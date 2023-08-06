import fnmatch
import logging
import logging.config
import pathlib
from typing import Optional

import click

from copernicus_marine_client.catalogue_parser.catalogue_parser import (
    FTP_KEY,
    S3NATIVE_KEY,
    get_protocol_from_url,
    get_protocol_url_from_id,
)
from copernicus_marine_client.catalogue_parser.request_structure import (
    GetRequest,
    get_request_from_file,
)
from copernicus_marine_client.command_line_interface.group_login import (
    get_username_password,
)
from copernicus_marine_client.command_line_interface.utils import (
    MutuallyExclusiveOption,
)
from copernicus_marine_client.download_functions.download_ftp import (
    download_ftp,
)
from copernicus_marine_client.download_functions.download_s3native import (
    download_s3native,
)
from copernicus_marine_client.utils import (
    DEFAULT_CLIENT_BASE_DIRECTORY,
    OVERWRITE_LONG_OPTION,
    OVERWRITE_OPTION_HELP_TEXT,
    OVERWRITE_SHORT_OPTION,
)

PROTOCOL_KEYS_ORDER = {"s3native": S3NATIVE_KEY, "ftp": FTP_KEY}

CREDENTIALS_REQUIRED_PROTOCOLS = [
    "ftp",
]


@click.group()
def cli_group_get() -> None:
    pass


@cli_group_get.command(
    "get",
    short_help="Download originally produced data files",
    help="""
    Download originally produced data files based on dataset_id or datafile URL path.
    The function fetches the files recursively if a folder path is passed as URL.
    When provided a dataset id,
    all the files in the corresponding folder will be downloaded.

    By default for any download request, a summary of the request result is
    displayed to the user and a confirmation is asked.
    This can be turned down.

    Example:

    \b
    > copernicus-marine get -nd -o data_folder --dataset-id cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m

    \b
    > copernicus-marine get -nd -o data_folder --dataset-url ftp://my.cmems-du.eu/Core/NWSHELF_MULTIYEAR_BGC_004_011/cmems_mod_nws_bgc-pft_myint_7km-3D-diato_P1M-m
    """,  # noqa
)
@click.option(
    "--dataset-url",
    "-u",
    type=str,
    help="Path to the data files",
)
@click.option(
    "--dataset-id",
    "-i",
    type=str,
    help="The dataset id",
)
@click.option(
    "--username",
    type=str,
    envvar="COPERNICUS_MARINE_SERVICE_USERNAME",
    default=None,
    help="If not set, search for environment variable"
    + " COPERNICUS_MARINE_SERVICE_USERNAME"
    + ", or else look for configuration files, or else ask for user input",
)
@click.option(
    "--password",
    type=str,
    envvar="COPERNICUS_MARINE_SERVICE_PASSWORD",
    default=None,
    help="If not set, search for environment variable"
    + " COPERNICUS_MARINE_SERVICE_PASSWORD"
    + ", or else look for configuration files, or else ask for user input",
)
@click.option(
    "--no-directories",
    "-nd",
    is_flag=True,
    help="Option to not recreate folder hierarchy" + " in ouput directory.",
    default=False,
)
@click.option(
    "--show-outputnames",
    is_flag=True,
    help="Option to display the names of the"
    + " output files before download.",
    default=False,
)
@click.option(
    "--output-directory",
    "-o",
    type=click.Path(path_type=pathlib.Path),
    help="The destination directory for the downloaded files."
    + " Default is the current directory",
)
@click.option(
    "--config-file-directory",
    type=click.Path(exists=True, path_type=pathlib.Path),
    default=DEFAULT_CLIENT_BASE_DIRECTORY,
    help="Path to a directory where a configuration file is stored. Accepts "
    + ".copernicus_marine_client_credentials / .netrc or _netrc / "
    + ".motuclient-python.ini files",
)
@click.option(
    "--force-download",
    is_flag=True,
    default=False,
    help="Flag to skip confirmation before download",
)
@click.option(
    OVERWRITE_LONG_OPTION,
    OVERWRITE_SHORT_OPTION,
    is_flag=True,
    default=False,
    help=OVERWRITE_OPTION_HELP_TEXT,
)
@click.option(
    "--force-protocol",
    type=click.Choice(list(PROTOCOL_KEYS_ORDER.keys())),
    help="Force download through one of the available protocols",
)
@click.option(
    "--request-file",
    type=click.Path(exists=True, path_type=pathlib.Path),
    help="Option to pass a file containg CLI arguments. "
    "The file MUST follow the structure of dataclass 'GetRequest'. ",
)
@click.option(
    "--overwrite-metadata-cache",
    cls=MutuallyExclusiveOption,
    type=bool,
    is_flag=True,
    default=False,
    help="Force to refresh the catalogue by overwriting the local cache",
    mutually_exclusive=["no_metadata_cache"],
)
@click.option(
    "--no-metadata-cache",
    cls=MutuallyExclusiveOption,
    type=bool,
    is_flag=True,
    default=False,
    help="Bypass the use of cache",
    mutually_exclusive=["overwrite_metadata_cache"],
)
@click.option(
    "--log-level",
    type=click.Choice(["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL", "QUIET"]),
    default="INFO",
    help=(
        "Set the details printed to console by the command "
        "(based on standard logging library)."
    ),
)
@click.option(
    "--filter",
    "--filter-with-globbing-pattern",
    type=str,
    default=None,
    help="A pattern that must match the absolute paths of "
    "the files to download. ",
)
@click.option(
    "--regex",
    "--filter-with-regular-expression",
    type=str,
    default=None,
    help="The regular expression that must match the absolute paths of "
    "the files to download. ",
)
def get(
    dataset_url: str,
    dataset_id: str,
    username: Optional[str],
    password: Optional[str],
    no_directories: bool,
    show_outputnames: bool,
    output_directory: Optional[pathlib.Path],
    config_file_directory: pathlib.Path,
    force_download: bool,
    overwrite_output_data: bool,
    request_file: Optional[pathlib.Path],
    force_protocol: str,
    overwrite_metadata_cache: bool,
    no_metadata_cache: bool,
    log_level: str,
    filter: Optional[str],
    regex: Optional[str],
):
    if log_level == "QUIET":
        logging.root.disabled = True
        logging.root.setLevel(level="CRITICAL")
    else:
        logging.root.setLevel(level=log_level)
    get_request = GetRequest()
    if request_file:
        get_request = get_request_from_file(request_file)
    request_update_dict = {
        "dataset_url": dataset_url,
        "dataset_id": dataset_id,
        "output_directory": output_directory,
        "force_protocol": force_protocol,
    }
    get_request.update(request_update_dict)

    # Specific treatment for default values:
    # In order to not overload arguments with default values
    if no_directories:
        get_request.no_directories = no_directories
    if show_outputnames:
        get_request.show_outputnames = show_outputnames
    if force_download:
        get_request.force_download = force_download
    if overwrite_output_data:
        get_request.overwrite = overwrite_output_data
    if force_protocol:
        get_request.force_protocol = force_protocol
    if filter:
        get_request.regex = fnmatch.translate(filter)
    if regex:
        get_request.regex = (
            regex
            if not filter
            else "(" + regex + "|" + fnmatch.translate(filter) + ")"
        )

    get_function(
        username,
        password,
        get_request,
        config_file_directory,
        overwrite_metadata_cache,
        no_metadata_cache,
    )


def get_function(
    username: Optional[str],
    password: Optional[str],
    get_request: GetRequest,
    config_file_directory: pathlib.Path,
    overwrite_metadata_cache: bool,
    no_metadata_cache: bool,
):
    # --- Protocol section
    if get_request.force_protocol:
        logging.info(
            f"You forced selection of protocol: {get_request.force_protocol}"
        )
    possible_protocols = (
        list(PROTOCOL_KEYS_ORDER.values())
        if not get_request.force_protocol
        else [PROTOCOL_KEYS_ORDER[get_request.force_protocol]]
    )
    if not get_request.dataset_url:
        if not get_request.dataset_id:
            syntax_error = SyntaxError(
                "Must specify at least one of 'dataset_url' or 'dataset_id'"
            )
            logging.error(syntax_error)
            raise syntax_error
        protocol, get_request.dataset_url = get_protocol_url_from_id(
            get_request.dataset_id,
            possible_protocols,
            overwrite_metadata_cache,
            no_metadata_cache,
        )
    else:
        protocol = get_protocol_from_url(get_request.dataset_url)
        if (
            get_request.force_protocol is not None
            and protocol != PROTOCOL_KEYS_ORDER[get_request.force_protocol]
        ):
            value_error = ValueError(
                f"Forced protocol {get_request.force_protocol} does not match "
                f"user-specified url {get_request.dataset_url}"
            )
            logging.error(value_error)
            raise value_error
    username, password = get_username_password(
        username,
        password,
        config_file_directory,
    )
    # --- Download redirection by protocol
    logging.info(f"Downloading using protocol {protocol}...")
    if protocol == FTP_KEY:
        download_summary = download_ftp(
            username,
            password,
            get_request,
        )
        logging.info(download_summary)
    elif protocol == S3NATIVE_KEY:
        download_summary = download_s3native(
            username,
            password,
            get_request,
        )
        logging.info(download_summary)
    else:
        type_error = TypeError(f"Protocol type not handled: {protocol}")
        logging.error(type_error)
        raise type_error
