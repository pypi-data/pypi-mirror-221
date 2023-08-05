# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from typing import Any

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEXTUAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from textual.app import App

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from lifegu42d.screens.chat_screen import ChatScreen
from lifegu42d.screens.logo_screen import LogoScreen
from lifegu42d.utils.functions.system import read_config, write_config


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ LIFEGU42D APP
# └─────────────────────────────────────────────────────────────────────────────────────


class Lifegu42dApp(App[None]):
    """The LIFEGU42D TUI application"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of config
    config: dict[str, str]

    # Define screens
    SCREENS = {
        "chat": ChatScreen,
        "logo": LogoScreen,
    }

    # Define default CSS
    DEFAULT_CSS = """
    Screen {
        align: center middle;
    }
    """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Init Method"""

        # Call super init method
        super().__init__(*args, **kwargs)

        # Load config
        self.load_config()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ ON READY
    # └─────────────────────────────────────────────────────────────────────────────────

    def on_ready(self) -> None:
        """On Ready Method"""

        # Push the logo screen
        self.push_screen("logo")

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ LOAD CONFIG
    # └─────────────────────────────────────────────────────────────────────────────────

    def load_config(self) -> None:
        """Loads a config file into the application state"""

        # Read config file
        self.config = read_config("lifegu42d")

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ UPDATE CONFIG
    # └─────────────────────────────────────────────────────────────────────────────────

    def update_config(self, **kwargs: str) -> None:
        """Updates the config file in memory and writes to disk"""

        # Return if no kwargs
        if not kwargs:
            return

        # Update config
        self.config.update(**kwargs)

        # Write config
        write_config("lifegu42d", self.config)
