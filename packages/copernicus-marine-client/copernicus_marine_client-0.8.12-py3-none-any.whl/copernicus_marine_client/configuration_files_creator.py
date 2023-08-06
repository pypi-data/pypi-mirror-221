import base64
import configparser
import logging
import os
import pathlib
from dataclasses import dataclass
from datetime import timedelta
from netrc import netrc
from typing import Literal, Optional

import click
import lxml.html
import requests
from cachier import cachier


def load_credential_from_copernicus_marine_config_file(
    credential_type: Literal["username", "password"],
    config_filename: pathlib.Path,
) -> Optional[str]:
    config_file = open(config_filename)
    config_string = base64.standard_b64decode(config_file.read()).decode(
        "utf8"
    )
    config = configparser.RawConfigParser()
    config.read_string(config_string)
    credential = config.get("credentials", credential_type)
    if credential:
        logging.debug(f"{credential_type} loaded from {config_filename}")
    return credential


def load_credential_from_netrc_config_file(
    credential_type: Literal["username", "password"],
    config_filename: pathlib.Path,
    host: str,
) -> Optional[str]:
    authenticator = netrc(config_filename).authenticators(host=host)
    if authenticator:
        username, _, password = authenticator
        logging.debug(f"{credential_type} loaded from {config_filename}")
        return username if credential_type == "username" else password
    else:
        return None


def load_credential_from_motu_config_file(
    credential_type: Literal["username", "password"],
    config_filename: pathlib.Path,
) -> Optional[str]:
    motu_file = open(config_filename)
    motu_credential_type = "user" if credential_type == "username" else "pwd"
    config = configparser.RawConfigParser()
    config.read_string(motu_file.read())
    credential = config.get("Main", motu_credential_type)
    if credential:
        logging.debug(f"{credential_type} loaded from {config_filename}")
    return credential


def retrieve_credential_from_config_files(
    credential_type: Literal["username", "password"],
    config_file_directory: pathlib.Path,
    host: str = "default_host",
) -> Optional[str]:

    copernicus_marine_client_config_filename = pathlib.Path(
        config_file_directory, ".copernicus_marine_client_credentials"
    )
    netrc_type = "_netrc" if os.system == "win32" else ".netrc"
    netrc_filename = pathlib.Path(config_file_directory, netrc_type)
    motu_filename = pathlib.Path(
        config_file_directory, ".motuclient-python.ini"
    )
    if copernicus_marine_client_config_filename.exists():
        credential = load_credential_from_copernicus_marine_config_file(
            credential_type, copernicus_marine_client_config_filename
        )

    elif netrc_filename.exists():
        credential = load_credential_from_netrc_config_file(
            credential_type, netrc_filename, host=host
        )
    elif motu_filename.exists():
        credential = load_credential_from_motu_config_file(
            credential_type, motu_filename
        )
    else:
        credential = None
    return credential


def create_copernicus_marine_client_config_file(
    username: str,
    password: str,
    config_file_directory: pathlib.Path,
    overwrite_configuration_file: bool,
) -> None:
    config_lines = [
        "[credentials]\n",
        f"username={username}\n",
        f"password={password}\n",
    ]
    config_filename = pathlib.Path(
        config_file_directory, ".copernicus_marine_client_credentials"
    )
    if config_filename.exists() and not overwrite_configuration_file:
        click.confirm(
            f"File {config_filename} already exists, overwrite it ?",
            abort=True,
        )
    config_file = open(config_filename, "w")
    config_string = base64.b64encode(
        "".join(config_lines).encode("ascii", "strict")
    ).decode("utf8")
    config_file.write(config_string)
    config_file.close()


@dataclass
class CheckCredentialsResponse:
    error: Optional[ConnectionRefusedError]


@cachier(stale_after=timedelta(hours=5))
def check_copernicus_marine_credentials(
    username: Optional[str], password: Optional[str]
) -> CheckCredentialsResponse:
    """
    Check provided Copernicus Marine Credentials are correct.

    Parameters
    ----------
    username : str
        Copernicus Marine Username, provided for free from https://marine.copernicus.eu
    password : str
        Copernicus Marine Password, provided for free from https://marine.copernicus.eu

    """
    cmems_cas_url = "https://cmems-cas.cls.fr/cas/login"
    conn_session = requests.session()
    login_session = conn_session.get(cmems_cas_url)
    login_from_html = lxml.html.fromstring(login_session.text)
    hidden_elements_from_html = login_from_html.xpath(
        '//form//input[@type="hidden"]'
    )
    playload = {
        he.attrib["name"]: he.attrib["value"]
        for he in hidden_elements_from_html
    }
    playload["username"] = username
    playload["password"] = password
    response = conn_session.post(cmems_cas_url, data=playload)
    if response.text.find("success") == -1:
        check_credentials_response = CheckCredentialsResponse(
            error=ConnectionRefusedError(
                "Incorrect username or password.\n"
                "Learn how to recover your credentials at: "
                "https://help.marine.copernicus.eu/en/articles/"
                "4444552-i-forgot-my-username-or-my-password-what-should-i-do"
            )
        )
        logging.error(check_credentials_response.error)
        return check_credentials_response
    return CheckCredentialsResponse(error=None)


def main(
    username: str,
    password: str,
    config_file_directory: pathlib.Path,
    overwrite_configuration_file: bool,
) -> None:
    if not config_file_directory.exists():
        pathlib.Path.mkdir(config_file_directory, parents=True)
    create_copernicus_marine_client_config_file(
        username=username,
        password=password,
        config_file_directory=config_file_directory,
        overwrite_configuration_file=overwrite_configuration_file,
    )
