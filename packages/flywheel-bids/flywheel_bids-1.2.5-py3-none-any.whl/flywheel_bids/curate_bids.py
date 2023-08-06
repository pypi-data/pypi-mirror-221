import argparse
import json
import logging
import os
import pickle
import re
import sys
import tempfile
from pathlib import Path

import flywheel

from .supporting_files import bidsify_flywheel, utils
from .supporting_files.templates import load_template
from .supporting_files.project_tree import get_project_node, set_tree

logger = logging.getLogger("curate-bids")


def clear_meta_info(context, template):
    if "info" in context:
        if template.namespace in context["info"]:
            del context["info"][template.namespace]
        if "IntendedFor" in context["info"]:
            del context["info"]["IntendedFor"]


def format_validation_error(err):
    path = "/".join(err.path)
    if path:
        return path + " " + err.message
    return err.message


def print_error_log(container, templateDef, errors):
    BIDS = container["info"].get("BIDS")
    bids_template = BIDS.get("template")

    error_message = ""

    if not bids_template:
        error_message += (
            "There was no BIDS template assigned in 'info.BIDS.template'. "
            "BIDS also encountered the following errors:\n"
        )
    else:
        error_message += (
            f"The BIDS template {bids_template} for this file encountered "
            f"the following errors:\n"
        )

    for ie, ee in enumerate(errors):
        error_message += (
            f"{ie+1}:\n............................................................\n"
        )

        if ee.validator == "required":
            match = re.match("'(?P<prop>.*)' is a required property", ee.message)
            required_prop = match.group("prop")
            schema = templateDef.get("properties", {}).get(required_prop)
            schema.pop("auto_update", "")

            if schema is None:
                error_message += (
                    f"Schema for {required_prop} not found in template:\n"
                    f"{json.dumps(templateDef.get('properties'), indent=2)}"
                )
            else:
                error_message += (
                    f"The required property '{required_prop}' is missing or invalid.\n"
                    f"This property must exist, and must match the following conditons:\n"
                    f"{json.dumps(schema, indent=2)}\n\n"
                )

        else:
            prop = ee.path[0]
            schema = templateDef.get("properties", {}).get(prop)
            schema.pop("auto_update", "")

            error_message += (
                f"Property '{ee.schema.get('title')}' violates the"
                f" '{ee.validator}' requirement: {ee.message}\n"
            )
            error_message += (
                f"Property must match the following conditions:\n"
                f"{json.dumps(schema, indent=2)}\n\n"
            )

    return error_message


def validate_meta_info(container, template):
    """Validate meta information

    Adds 'BIDS.NA' if no BIDS info present
    Adds 'BIDS.valid' and 'BIDS.error_message'
        to communicate to user if values are valid (!!! minimal being checked)

    TODO: validation needs to check for more than non-empty strings; e.g., alphanumeric

    """
    # Get namespace
    namespace = template.namespace

    # If 'info' is NOT in container, then must not
    #   have matched to a template, create 'info'
    #  field with object {'BIDS': 'NA'}
    if "info" not in container:
        container["info"] = {namespace: "NA"}
    # if the namespace ('BIDS') is NOT in 'info',
    #   then must not have matched to a template,
    #   add  {'BIDS': 'NA'} to the meta info
    elif namespace not in container["info"]:
        container["info"][namespace] = "NA"
    # If already assigned BIDS 'NA', then break
    elif container["info"][namespace] == "NA":
        pass
    # Otherwise, iterate over keys within container
    else:
        valid = True
        error_message = ""

        # Find template
        templateName = container["info"][namespace].get("template")
        if templateName:
            templateDef = template.definitions.get(templateName)
            if templateDef:
                errors = template.validate(templateDef, container["info"][namespace])
                if errors:
                    log_error = print_error_log(container, templateDef, errors)
                    logger.debug(log_error)

                    valid = False
                    error_message = "\n".join(
                        [format_validation_error(err) for err in errors]
                    )
            else:
                valid = False
                error_message += "Unknown template: %s. " % templateName

        # Assign 'valid' and 'error_message' values
        container["info"][namespace]["valid"] = valid
        container["info"][namespace]["error_message"] = error_message


def update_meta_info(fw, context):
    """Update file information"""
    # Modify file
    if context["container_type"] == "file":
        # Modify acquisition file
        if context["parent_container_type"] == "acquisition":
            fw.set_acquisition_file_info(
                context["acquisition"]["id"],
                context["file"]["name"],
                context["file"]["info"],
            )
        # Modify project file
        elif context["parent_container_type"] == "project":
            fw.set_project_file_info(
                context["project"]["id"],
                context["file"]["name"],
                context["file"]["info"],
            )
        # Modify session file
        elif context["parent_container_type"] == "session":
            fw.set_session_file_info(
                context["session"]["id"],
                context["file"]["name"],
                context["file"]["info"],
            )
        else:
            logger.info(
                "Cannot determine file parent container type: "
                + context["parent_container_type"]
            )
    # Modify project
    elif context["container_type"] == "project":
        fw.replace_project_info(context["project"]["id"], context["project"]["info"])
    # Modify session
    elif context["container_type"] == "session":
        fw.replace_session_info(context["session"]["id"], context["session"]["info"])
    # Modify acquisition
    elif context["container_type"] == "acquisition":
        fw.replace_acquisition_info(
            context["acquisition"]["id"], context["acquisition"]["info"]
        )
    # Cannot determine container type
    else:
        logger.info("Cannot determine container type: " + context["container_type"])


class Count:
    def __init__(self):
        self.containers = 0  # counts project, sessions and acquisitions
        self.sessions = 0
        self.acquisitions = 0
        self.files = 0


def save_project_sidecar(project, project_node, save_sidecar_as_metadata):
    """Save "dataset_description.json" sidecar file

    Remove info that was just put on the project_node and attach it as a json file
    on the project if it does not yet exist.

    Args:
        project (Project container)
        project_node (TreeNode) a "context" representation of the project
        save_sidecar_as_metadata (bool): if true, save sidecar data as metadata also
    """

    SIDECAR_NAME = "dataset_description.json"
    proj_sidecars = [file for file in project.files if file.name == SIDECAR_NAME]

    if len(proj_sidecars) > 1:
        logger.debug("ERROR: multiple '%s' files exist", SIDECAR_NAME)
    elif len(proj_sidecars) == 1:
        logger.info("'%s' file already exists", SIDECAR_NAME)
    else:  # create and attach file to project
        logger.info("'%s' file does not exist, creating it...", SIDECAR_NAME)
        if "info" in project_node:
            if "BIDS" in project_node.data["info"]:
                json_data = project_node.data["info"]["BIDS"]
                if "template" in json_data:
                    del json_data["template"]
                if "rule_id" in json_data:
                    del json_data["rule_id"]
                json_str = json.dumps(json_data, indent=4)
                file_spec = flywheel.FileSpec(SIDECAR_NAME, json_str, "text/plain")
                project.upload_file(file_spec)

                if not save_sidecar_as_metadata:  # remove BIDS namespace
                    del project_node.data["info"]["BIDS"]
                # else: that BIDS info will be updated in project metadata
            else:
                logger.debug("ERROR: no BIDS information exists")
        else:
            logger.debug("ERROR: no project.info exists")


def curate_bids(
    fw,
    project_id,
    subject_id="",
    session_id="",
    reset=False,
    dont_recurate_project=False,
    template_name="",
    template_path="",
    pickle_tree=False,
    dry_run=False,
    save_sidecar_as_metadata=False,
):
    """Curate BIDS.

    If curating an entire project, loop over subjects to find all sessions.  Curate all sessions for a given
    subject at the same time so "resolvers" can work on all sessions for the subject.
    This can run on only one subject or session if desired by providing an ID.

    Args:
        fw (Flywheel Client): The Flywheel Client
        project_id (str): The Flywheel Project container ID.
        subject_id (str): The Flywheel subject container ID (will only curate this subject).
        session_id (str): The Flywheel session container ID (will only curate this session).
        reset (bool): Whether to erase info.BIDS before curation.
        dont_recurate_project (bool): If project container is already curated, make this True
        template_name (str): Which template type to use. Options include:
                Default, BIDS-v1, ReproIn.
        template_path (str): Provide a specific template file. Supersedes template_name.
        save_sidecar_as_metadata (bool): sidecar data is in file.info (metadata) so for
                IntendedFors, update metadata instead of updating the actual json sidecar.

    """

    count = Count()

    project = fw.get_project(project_id)

    template = load_template(fw, template_path, template_name, save_sidecar_as_metadata)

    p_name = f"project_node_{project_id}.pickle"
    if pickle_tree and Path(p_name).exists():
        logger.info("Using pickled %s", p_name)
        with open(p_name, "rb") as f:
            project_node = pickle.load(f)
    else:
        project_node = get_project_node(fw, project_id)

        if pickle_tree:
            with open(p_name, "wb") as f:
                pickle.dump(project_node, f)

    # Curate the project all by itself
    count = curate_bids_tree(
        fw,
        template,
        project_node,
        count,
        reset=reset,
        dont_recurate_project=dont_recurate_project,
        dry_run=dry_run,
    )

    save_project_sidecar(project, project_node, save_sidecar_as_metadata)

    if session_id:
        logger.info("Getting single session ID=%s", session_id)
        session = fw.get_session(session_id)
        subject_id = session.subject.id

    if subject_id:
        logger.info("Getting single subject ID=%s", subject_id)
    else:
        logger.info("Getting all subjects")

    for subject in project.subjects.iter():
        if subject_id and subject_id != subject.id:
            continue

        p_name = f"subject_node_{subject.id}.pickle"
        if pickle_tree and Path(p_name).exists():
            logger.info("Using pickled %s", p_name)
            with open(p_name, "rb") as f:
                project_node = pickle.load(f)
        else:
            set_tree(
                fw, project_node, subject, session_id
            )  # if session_id is set, this skips everything but that one

            if pickle_tree:
                with open(p_name, "wb") as f:
                    pickle.dump(project_node, f)

        count = curate_bids_tree(
            fw,
            template,
            project_node,
            count,
            reset=reset,
            dont_recurate_project=True,
            dry_run=dry_run,
        )

        project_node.children.clear()  # no need to keep previous subjects

    logger.info("Curated %s session containers", count.sessions)
    logger.info("Curated %s acquisition containers", count.acquisitions)
    logger.info("Curated %s files", count.files)
    num_proj_ses_acq = 1 + count.sessions + count.acquisitions
    if count.containers != num_proj_ses_acq:
        logger.warning(
            "Container_counter should be %s but it is %s",
            num_proj_ses_acq,
            count.containers,
        )


def curate_bids_tree(
    fw,
    template,
    project_node,
    count,
    reset=False,
    dont_recurate_project=False,
    dry_run=False,
):
    """Curate BIDS tree.

    Given a BIDS project curation template and Flywheel hierarchy context, figure out the proper
    metadata fields to be able to save data in BIDS format.  The context must include the project
    information to be able to curate any subject or session.  The context should include no more
    than one subject in case there are very many subjects.  The context may consist of a single
    session.

    "Resolvers" are used here to fill in information across sessions.  The only current example
    is the "IntendedFor" BIDS field which is used to list the scans that a field map intends to
    correct.  All sessions for a given subject need to be processed at the same time to allow
    this to happen.

    Args:
        fw (Flywheel Client): The Flywheel Client
        template (template.Template): A collection of definitions and rules to populate definition values
        project_node (TreeNode): The context for BIDS processing: a tree of containers and files on them
        count (Count): The number of project|session|acquisition|files containers processed
        reset (bool): Whether to erase info.BIDS before curation.
        dont_recurate_project (bool): The project_node is always provided, this lets it not be re-curated
    Return:
        count (Count)
    """
    # Curation begins: match, resolve, update

    # Match: do initial template matching and updating

    for context in project_node.context_iter():
        ctype = context["container_type"]
        parent_ctype = context["parent_container_type"]

        if ctype == "project" and dont_recurate_project:
            pass  # don't curate OR reset
        else:
            # Cleanup, if indicated
            if reset:
                clear_meta_info(context[ctype], template)

            elif context[ctype].get("info", {}).get("BIDS") == "NA":
                continue

        # BIDSIFY: note that subjects are not bidsified because they have no BIDS information on them.
        if ctype in ["project", "session", "acquisition"]:
            if ctype == "project":
                if dont_recurate_project:
                    logger.debug("Not re-curating project container")
                    continue

            logger.info(
                f"{count.containers}: Bidsifying Container: <{ctype}> <{context.get(ctype).get('label')}>"
            )

            count.containers += 1
            if ctype == "session":
                count.sessions += 1
            elif ctype == "acquisition":
                count.acquisitions += 1

            bidsify_flywheel.process_matching_templates(context, template)

            # Add run counter for session
            if ctype == "session":
                logger.debug(
                    f"adding run counter for session {context.get(ctype).get('label')}"
                )
                context["run_counters"] = utils.RunCounterMap()

        elif ctype == "file":
            logger.debug(
                f"Bidsifying file: <{ctype}> <{context.get(ctype).get('name')}>"
            )

            count.files += 1

            # Process matching
            context["file"] = bidsify_flywheel.process_matching_templates(
                context, template
            )

            # Validate meta information
            validate_meta_info(context["file"], template)

    if not dry_run:
        # Resolve: perform path resolutions, if needed.  Currently only used to handle "IntendedFor" field which
        # needs to happen after a subject has been curated.
        for context in project_node.context_iter():
            bidsify_flywheel.process_resolvers(context, template)

        # Update: send updates to Flywheel, if the Flywheel Client is instantiated
        if fw:
            logger.info("Updating BIDS metadata on Flywheel")
            for context in project_node.context_iter():
                ctype = context["container_type"]
                node = context[ctype]
                if node.is_dirty():
                    update_meta_info(fw, context)
        else:
            logger.info("Missing fw, cannot update BIDS metadata on Flywheel")
    else:
        logger.info("Dry run, NOT updating BIDS metadata on Flywheel")

    return count


def configure_logging(verbosity):
    my_logs = ["curate-bids"]

    loggers = [
        logging.getLogger(name)
        for name in logging.root.manager.loggerDict
        if name in my_logs
    ]

    # Custom levels of 0 and 1 may be sent from legacy code;
    # 20 == INFO and 10 == DEBUG in modern python logging
    if verbosity == 0 or verbosity == 20:
        print('setting log level to "info"')
        logging.basicConfig(
            format="[ %(module)s %(asctime)2s %(levelname)2s] %(message)s"
        )
        logger.setLevel(logging.INFO)

    elif verbosity == 1 or verbosity == 10:
        print('setting log level to "debug"')
        logging.basicConfig(
            format="[ %(module)s %(asctime)2s %(levelname)2s: %(lineno)s] %(message)s"
        )
        logger.setLevel(logging.DEBUG)


def main_with_args(
    api_key,
    session_id,
    reset,
    session_only,
    template_name,
    template_path=None,
    subject_id="",
    project_label="",
    group_id="",
    verbosity=1,
    pickle_tree=False,
    dry_run=False,
    save_sidecar_as_metadata=False,
):
    """Run BIDS Curation, called by curate-bids Gear or CLI."""
    fw = flywheel.Client(api_key)

    configure_logging(verbosity)

    if group_id:
        project_id = utils.validate_project_label(fw, project_label, group_id=group_id)
    elif project_label:
        project_id = utils.validate_project_label(fw, project_label)
    elif subject_id:
        project_id = utils.get_project_id_from_subject_id(fw, subject_id)
    elif session_id:
        project_id = utils.get_project_id_from_session_id(fw, session_id)
    else:
        logger.error(
            "Either project label (group id optional) or subject/session id is required!"
        )
        sys.exit(1)

    # no longer passing session_only along.  Empty session_id means get all sessions.
    if not session_only:
        session_id = ""

    # Curate BIDS
    curate_bids(
        fw,
        project_id,
        subject_id=subject_id,
        session_id=session_id,
        reset=reset,
        dont_recurate_project=False,
        template_name=template_name,
        template_path=template_path,
        pickle_tree=pickle_tree,
        dry_run=dry_run,
        save_sidecar_as_metadata=save_sidecar_as_metadata,
    )


def main():
    parser = argparse.ArgumentParser(description="BIDS Curation")
    parser.add_argument(
        "--api-key", dest="api_key", action="store", required=True, help="API key"
    )
    parser.add_argument(
        "-p",
        dest="project_label",
        action="store",
        required=False,
        default=None,
        help="A Flywheel instance Project label.",
    )
    parser.add_argument(
        "-g",
        dest="group_id",
        action="store",
        required=False,
        default=None,
        help="A Flywheel instance Group ID.",
    )
    parser.add_argument(
        "--subject",
        dest="subject_id",
        action="store",
        required=False,
        default="",
        help="A Flywheel instance Subject ID; alternative to determine Project label.",
    )
    parser.add_argument(
        "--session",
        dest="session_id",
        action="store",
        required=False,
        default="",
        help="A Flywheel instance Session ID; alternative to determine Project label.",
    )
    parser.add_argument(
        "--reset",
        dest="reset",
        action="store_true",
        default=False,
        help="Hard reset of BIDS metadata before running.",
    )
    parser.add_argument(
        "--dont_recurate_project",
        dest="dont_recurate_project",
        action="store_true",
        default=False,
        help="Don't re-curate the project.",
    )
    parser.add_argument(
        "--template-type",
        dest="template_name",
        action="store",
        required=False,
        default=None,
        help="Which template type to use. Options include : Default, ReproIn, or Custom.",
    )
    parser.add_argument(
        "--template-file",
        dest="template_path",
        action="store",
        default=None,
        help="Template file to use. Supersedes the --template-type flag.",
    )
    parser.add_argument(
        "--pickle_tree",
        dest="pickle_tree",
        action="store_true",
        default=False,
        help="Use pickled context if available, save if not (used for debugging).",
    )
    parser.add_argument(
        "--dry_run",
        dest="dry_run",
        action="store_true",
        default=False,
        help="Dry run does not update Flywheel metadata.",
    )
    parser.add_argument(
        "--verbosity",
        dest="verbosity",
        action="store",
        type=int,
        default=1,
        help="Debug level (0, 10, 2, 20)",
    )
    parser.add_argument(
        "--save_sidecar_as_metadata",
        choices=["yes", "no", "auto"],
        default="auto",
        required=False,
        help="The BIDS sidecar is metadata in file.info. (default = auto)",
    )

    args = parser.parse_args()

    configure_logging(int(args.verbosity))

    # Prep
    # Check API key - raises Error if key is invalid
    fw = flywheel.Client(args.api_key)

    if args.group_id:
        project_id = utils.validate_project_label(
            fw, args.project_label, group_id=args.group_id
        )
    elif args.project_label:
        project_id = utils.validate_project_label(fw, args.project_label)
    elif args.subject_id:
        project_id = utils.get_project_id_from_subject_id(fw, args.subject_id)
    elif args.session_id:
        project_id = utils.get_project_id_from_session_id(fw, args.session_id)
    else:
        logger.error(
            "Either project label (group id optional) or subject/session id is required!"
        )
        sys.exit(1)

    if args.save_sidecar_as_metadata == "yes":
        save_sidecar_as_metadata = True
    elif args.save_sidecar_as_metadata == "no":
        save_sidecar_as_metadata = False
    else:  # check to see if the project has "BIDS" metadata
        project = fw.get_project(project_id)
        if "BIDS" in project.info:
            save_sidecar_as_metadata = True
        else:
            save_sidecar_as_metadata = False

    # Curate BIDS project
    curate_bids(
        fw,
        project_id,
        args.subject_id,
        args.session_id,
        reset=args.reset,
        dont_recurate_project=False,
        template_name=args.template_name,
        template_path=args.template_path,
        pickle_tree=args.pickle_tree,
        dry_run=args.dry_run,
        save_sidecar_as_metadata=save_sidecar_as_metadata,
    )


if __name__ == "__main__":
    main()
