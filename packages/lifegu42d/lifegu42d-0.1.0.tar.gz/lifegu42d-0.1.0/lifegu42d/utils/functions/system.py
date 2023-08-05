# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import json
import os

from platformdirs import user_config_dir


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GET CONFIG FILE DIRECTORY
# └─────────────────────────────────────────────────────────────────────────────────────


def get_config_file_directory(app_name: str) -> str:
    """Returns a directory for an application's config file"""

    # Get config directory
    config_directory = user_config_dir(app_name)

    # Return config directory
    return config_directory


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GET CONFIG FILE PATH
# └─────────────────────────────────────────────────────────────────────────────────────


def get_config_file_path(app_name: str) -> str:
    """Returns a file path for an application's config file"""

    # Get config file directory
    config_directory = get_config_file_directory(app_name)

    # Create config file path
    config_file_path = os.path.join(config_directory, "config.json")

    # Return config file path
    return config_file_path


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ READ CONFIG
# └─────────────────────────────────────────────────────────────────────────────────────


def read_config(app_name: str) -> dict[str, str]:
    """Reads a config file"""

    # Get config file path
    config_file_path = get_config_file_path(app_name)

    # Check if config file exists
    if not os.path.exists(config_file_path):
        return {}

    # Read config file
    with open(config_file_path, "r") as f:
        config = json.load(f)

    # Return if config is not a dict
    if not isinstance(config, dict):
        return {}

    # Return config
    return config


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ WRITE CONFIG
# └─────────────────────────────────────────────────────────────────────────────────────


def write_config(app_name: str, config: dict[str, str]) -> None:
    """Writes a config file"""

    # Get config file directory
    config_file_directory = get_config_file_directory(app_name)

    # Create config file directory if it does not exist
    if not os.path.exists(config_file_directory):
        os.makedirs(config_file_directory)

    # Get config file path
    config_file_path = get_config_file_path(app_name)

    # Write config file
    with open(config_file_path, "w") as f:
        json.dump(config, f, indent=4)
