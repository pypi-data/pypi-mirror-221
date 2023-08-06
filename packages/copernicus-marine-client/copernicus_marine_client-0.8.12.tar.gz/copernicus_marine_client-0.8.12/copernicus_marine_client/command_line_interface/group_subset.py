import logging
import logging.config
import pathlib
import sys
from datetime import datetime
from typing import List, Optional

import click

from copernicus_marine_client.catalogue_parser.catalogue_parser import (
    GEOCHUNKED_KEY,
    MOTU_KEY,
    OPENDAP_KEY,
    TIMECHUNKED_KEY,
    get_dataset_from_id,
    get_dataset_url_from_id,
    get_protocol_from_url,
    parse_catalogue,
    protocol_not_available_error,
)
from copernicus_marine_client.catalogue_parser.request_structure import (
    SubsetRequest,
    convert_motu_api_request_to_structure,
    subset_request_from_file,
)
from copernicus_marine_client.command_line_interface.exception_handler import (
    log_exception_and_exit,
)
from copernicus_marine_client.command_line_interface.group_login import (
    get_username_password,
)
from copernicus_marine_client.command_line_interface.utils import (
    MutuallyExclusiveOption,
)
from copernicus_marine_client.download_functions.download_motu import (
    download_motu,
)
from copernicus_marine_client.download_functions.download_opendap import (
    download_opendap,
)
from copernicus_marine_client.download_functions.download_zarr import (
    download_zarr,
    get_optimized_chunking,
)
from copernicus_marine_client.utils import (
    DEFAULT_CLIENT_BASE_DIRECTORY,
    OVERWRITE_LONG_OPTION,
    OVERWRITE_OPTION_HELP_TEXT,
    OVERWRITE_SHORT_OPTION,
)

PROTOCOL_KEYS_ORDER = {
    "zarr": (TIMECHUNKED_KEY, GEOCHUNKED_KEY),
    "zarr-map": TIMECHUNKED_KEY,
    "zarr-timeserie": GEOCHUNKED_KEY,
    "opendap": OPENDAP_KEY,
    "motu": MOTU_KEY,
}


def to_command_line_interface_protocol(catalogue_protocol: str) -> str:
    return next(
        key
        for key, value in PROTOCOL_KEYS_ORDER.items()
        if value == catalogue_protocol
    )


def to_command_line_interface_protocols(
    catalogue_protocols: list[str],
) -> list[str]:
    return list(map(to_command_line_interface_protocol, catalogue_protocols))


CREDENTIALS_REQUIRED_PROTOCOLS = [
    "opendap",
    "motu",
]


@click.group()
def cli_group_subset() -> None:
    pass


@cli_group_subset.command(
    "subset",
    short_help="Downloads subsets of datasets as NetCDF files or Zarr stores",
    help="""
    Downloads subsets of datasets as NetCDF files or Zarr stores.
    Either one of 'dataset-id' or 'dataset-url' is required (can be found via the 'copernicus-marine describe' command).
    The arguments value passed individually through the CLI take precedence over the values from the "motu-api-request" option,
    which takes precedence over the ones from the "request-file" option

    Example:

    \b
    > copernicus-marine subset
    --dataset-id METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2
    --variable analysed_sst --variable sea_ice_fraction
    --start-datetime 2021-01-01 --end-datetime 2021-01-02
    --minimal-longitude 0.0 --maximal-longitude 0.1
    --minimal-latitude 0.0 --maximal-latitude 0.1

    \b
    > copernicus-marine subset -i METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2 -v analysed_sst -v sea_ice_fraction -t 2021-01-01 -T 2021-01-02 -x 0.0 -X 0.1 -y 0.0 -Y 0.1
    """,  # noqa
)
@click.option(
    "--dataset-url",
    "-u",
    type=str,
    help="The full dataset URL",
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
    "--variable",
    "-v",
    "variables",
    type=str,
    help="Specify dataset variables",
    multiple=True,
)
@click.option(
    "--minimal-longitude",
    "-x",
    type=float,
    help=(
        "Minimal longitude for the subset. "
        "The value will be reduced to the interval [-180; 360["
    ),
)
@click.option(
    "--maximal-longitude",
    "-X",
    type=float,
    help=(
        "Maximal longitude for the subset. "
        "The value will be reduced to the interval [-180; 360["
    ),
)
@click.option(
    "--minimal-latitude",
    "-y",
    type=click.FloatRange(min=-90, max=90),
    help="Minimal latitude for the subset. Requires a float within this range:",
)
@click.option(
    "--maximal-latitude",
    "-Y",
    type=click.FloatRange(min=-90, max=90),
    help="Maximal latitude for the subset. Requires a float within this range:",
)
@click.option(
    "--minimal-depth",
    "-z",
    type=click.FloatRange(min=0),
    help="Minimal depth for the subset. Requires a float within this range:",
)
@click.option(
    "--maximal-depth",
    "-Z",
    type=click.FloatRange(min=0),
    help="Maximal depth for the subset. Requires a float within this range:",
)
@click.option(
    "--vertical-dimension-as-originally-produced",
    type=bool,
    default=True,
    show_default=True,
    help=(
        "Consolidate the vertical dimension (the z-axis) as it is in the "
        "dataset originally produced, "
        "named `depth` with descending positive values."
    ),
)
@click.option(
    "--start-datetime",
    "-t",
    type=click.DateTime(
        ["%Y", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"]
    ),
    help="The start datetime of the temporal subset. Caution: encapsulate date "
    + 'with " " to ensure valid expression for format "%Y-%m-%d %H:%M:%S"',
)
@click.option(
    "--end-datetime",
    "-T",
    type=click.DateTime(
        ["%Y", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"]
    ),
    help="The end datetime of the temporal subset. Caution: encapsulate date "
    + 'with " " to ensure valid expression for format "%Y-%m-%d %H:%M:%S"',
)
@click.option(
    "--output-directory",
    "-o",
    type=click.Path(path_type=pathlib.Path),
    help="The destination folder for the downloaded files."
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
    "--output-filename",
    "-f",
    type=click.Path(path_type=pathlib.Path),
    help=(
        "Concatenate the downloaded data in the given file name "
        "(under the output directory). If "
        "the output-filename argument ends with '.nc' suffix, the file will be "
        "downloaded as a netCDF file."
    ),
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
    help="Option to pass a filename corresponding to a file containg CLI arguments. "
    "The file MUST follow the structure of dataclass 'SubsetRequest'. ",
)
@click.option(
    "--motu-api-request",
    type=str,
    help=(
        "Option to pass a complete MOTU api request as a string. "
        'Caution, user has to replace double quotes " with single '
        "quotes ' in the request"
    ),
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
@log_exception_and_exit
def subset(
    dataset_url: str,
    dataset_id: str,
    username: str,
    password: str,
    variables: Optional[List[str]],
    minimal_longitude: Optional[float],
    maximal_longitude: Optional[float],
    minimal_latitude: Optional[float],
    maximal_latitude: Optional[float],
    minimal_depth: Optional[float],
    maximal_depth: Optional[float],
    vertical_dimension_as_originally_produced: bool,
    start_datetime: Optional[datetime],
    end_datetime: Optional[datetime],
    output_filename: Optional[pathlib.Path],
    force_protocol: Optional[str],
    request_file: Optional[pathlib.Path],
    output_directory: Optional[pathlib.Path],
    config_file_directory: pathlib.Path,
    motu_api_request: Optional[str],
    force_download: bool,
    overwrite_output_data: bool,
    overwrite_metadata_cache: bool,
    no_metadata_cache: bool,
    log_level: str,
):
    if log_level == "QUIET":
        logging.root.disabled = True
        logging.root.setLevel(level="CRITICAL")
    else:
        logging.root.setLevel(level=log_level)
    subset_request = SubsetRequest()
    if request_file:
        subset_request = subset_request_from_file(request_file)
    if motu_api_request:
        motu_api_subset_request = convert_motu_api_request_to_structure(
            motu_api_request
        )
        subset_request.update(motu_api_subset_request.__dict__)
    request_update_dict = {
        "dataset_url": dataset_url,
        "dataset_id": dataset_id,
        "variables": variables,
        "minimal_longitude": minimal_longitude,
        "maximal_longitude": maximal_longitude,
        "minimal_latitude": minimal_latitude,
        "maximal_latitude": maximal_latitude,
        "minimal_depth": minimal_depth,
        "maximal_depth": maximal_depth,
        "vertical_dimension_as_originally_produced": vertical_dimension_as_originally_produced,  # noqa
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "output_directory": output_directory,
        "output_filename": output_filename,
        "force_protocol": force_protocol,
    }
    subset_request.update(request_update_dict)
    if all(
        e is None
        for e in [
            subset_request.variables,
            subset_request.minimal_longitude,
            subset_request.maximal_longitude,
            subset_request.minimal_latitude,
            subset_request.maximal_latitude,
            subset_request.minimal_depth,
            subset_request.maximal_depth,
            subset_request.start_datetime,
            subset_request.end_datetime,
        ]
    ):
        logging.error(
            "The requested dataset is not subset, "
            "please use the 'get' command instead."
        )
        sys.exit(1)
    # Specific treatment for default values:
    # In order to not overload arguments with default values
    if force_download:
        subset_request.force_download = force_download
    if overwrite_output_data:
        subset_request.overwrite = overwrite_output_data

    subset_function(
        username,
        password,
        subset_request,
        config_file_directory,
        overwrite_metadata_cache,
        no_metadata_cache,
    )


def subset_function(
    username: str,
    password: str,
    subset_request: SubsetRequest,
    config_file_directory: pathlib.Path,
    overwrite_metadata_cache: bool,
    no_metadata_cache: bool,
) -> str:
    def _flatten(item):
        if isinstance(item, (tuple, list)):
            return [a for i in item for a in _flatten(i)]
        else:
            return [item]

    catalogue = parse_catalogue(overwrite_metadata_cache, no_metadata_cache)
    # ---Protocol section
    possible_protocols = (
        [p for p in list(PROTOCOL_KEYS_ORDER.values()) if isinstance(p, str)]
        if not subset_request.force_protocol
        else _flatten(PROTOCOL_KEYS_ORDER[subset_request.force_protocol])
    )
    if subset_request.force_protocol:
        logging.info(
            f"You forced selection of protocol: {subset_request.force_protocol}"
        )
    if not subset_request.dataset_url:
        if not subset_request.dataset_id:
            syntax_error = SyntaxError(
                "Must specify at least one of 'dataset_url' or 'dataset_id'"
            )
            logging.error(syntax_error)
            raise syntax_error
        protocol_keys_iterator = iter(possible_protocols)
        while not subset_request.dataset_url:
            try:
                protocol = next(protocol_keys_iterator)
            except StopIteration as exception:
                catalogue_available_protocols = get_dataset_from_id(
                    catalogue, subset_request.dataset_id
                ).get_available_protocols()
                available_protocols = to_command_line_interface_protocols(
                    catalogue_available_protocols
                )
                raise protocol_not_available_error(
                    subset_request.dataset_id, available_protocols
                ) from exception
            subset_request.dataset_url = get_dataset_url_from_id(
                catalogue, subset_request.dataset_id, protocol
            )
    else:
        protocol = get_protocol_from_url(subset_request.dataset_url)
    username, password = get_username_password(
        username,
        password,
        config_file_directory,
    )
    # --- Download redirection by protocol
    if subset_request.force_protocol and (
        protocol != PROTOCOL_KEYS_ORDER[subset_request.force_protocol]
        and protocol not in PROTOCOL_KEYS_ORDER[subset_request.force_protocol]
    ):
        attribute_error = AttributeError(
            f"Dataset url ({subset_request.dataset_url}) does not match forced "
            f"protocol ({PROTOCOL_KEYS_ORDER[subset_request.force_protocol]})!"
        )
        logging.error(attribute_error)
        raise attribute_error
    elif protocol in [TIMECHUNKED_KEY, GEOCHUNKED_KEY]:
        # Check if both timechunked and geochunked data are available
        url_timechunked, url_geochunked = (
            map(
                get_dataset_url_from_id,
                [catalogue] * 2,
                [subset_request.dataset_id] * 2,
                [TIMECHUNKED_KEY, GEOCHUNKED_KEY],
            )
            if subset_request.dataset_id
            else (None, None)
        )
        if (
            url_timechunked
            and url_geochunked
            and (subset_request.force_protocol in [None, "zarr"])
        ):
            subset_request.dataset_url = (
                url_timechunked
                if get_optimized_chunking(subset_request)
                else url_geochunked
            )
        logging.info("Download Zarr files through S3")
        output_name = download_zarr(
            username,
            password,
            subset_request,
        )

    elif protocol == OPENDAP_KEY:
        logging.info("Download through OPeNDAP")
        output_name = download_opendap(
            username,
            password,
            subset_request,
        )
    elif protocol == MOTU_KEY:
        logging.info("Download through MOTU")
        output_name = download_motu(
            username,
            password,
            subset_request,
            catalogue=catalogue,
        )
    elif not protocol:
        key_error = KeyError(
            f"The requested dataset '{subset_request.dataset_id}' does not have "
            f"{possible_protocols} url available"
        )
        logging.error(key_error)
        raise
    else:
        key_error = KeyError(
            f"Protocol {protocol} not handled by subset command"
        )
        logging.error(key_error)
        raise key_error
    return output_name
