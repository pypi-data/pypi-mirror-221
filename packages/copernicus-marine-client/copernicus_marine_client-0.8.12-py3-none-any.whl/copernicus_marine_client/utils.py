import pathlib

OVERWRITE_SHORT_OPTION = "--overwrite"
OVERWRITE_LONG_OPTION = "--overwrite-output-data"
OVERWRITE_OPTION_HELP_TEXT = (
    "If specified and if the file already exists on destination, then it will be "
    "overwritten instead of creating new one with unique index."
)

FORCE_DOWNLOAD_CLI_PROMPT_MESSAGE = "Do you want to proceed with download?"

DEFAULT_CLIENT_BASE_DIRECTORY = (
    pathlib.Path.home() / ".copernicus_marine_client"
)


def get_unique_filename(
    filepath: pathlib.Path, overwrite_option: bool
) -> pathlib.Path:
    if not overwrite_option:
        parent = filepath.parent
        filename = filepath.stem
        extension = filepath.suffix
        counter = 1

        while filepath.exists():
            filepath = parent / (
                filename + "_(" + str(counter) + ")" + extension
            )
            counter += 1

    return filepath
