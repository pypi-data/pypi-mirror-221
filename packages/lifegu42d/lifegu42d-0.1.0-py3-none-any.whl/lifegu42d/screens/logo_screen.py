# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from typing import Any

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEXTUAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Footer, Static

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from lifegu42d.screens.chat_screen import ChatScreen


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CONSTANTS
# └─────────────────────────────────────────────────────────────────────────────────────

# Define logo
LOGO = """
db      d888888b d88888b d88888b  d888b  db    db   j88D  .d888b. d8888b.
88        `88'   88'     88'     88' Y8b 88    88  j8~88  VP  `8D 88  `8D
88         88    88ooo   88ooooo 88      88    88 j8' 88     odD' 88   88
88         88    88ooo   88ooooo 88  ooo 88    88 V88888D  .88'   88   88
88booo.   .88.   88      88.     88. ~8~ 88b  d88     88  j88.    88  .8D
Y88888P Y888888P YP      Y88888P  Y888P  ~Y8888P'     VP  888888D Y8888D'

                                                            by seamicole
"""


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ LOGO SCREEN
# └─────────────────────────────────────────────────────────────────────────────────────


class LogoScreen(Screen[Any]):
    """A logo screen for the LIFEGU42D application"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define bindings
    BINDINGS = [
        Binding("c", "push_chat_screen", "ChatGPT", show=True),
    ]

    # Define default CSS
    DEFAULT_CSS = """
    .logo {
        content-align: center middle;
    }
    """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ COMPOSE
    # └─────────────────────────────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        """Compose Method"""

        # Yield logo
        yield Static(LOGO, classes="logo")

        # Yield footer
        yield Footer()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ ACTION PUSH CHAT SCREEN
    # └─────────────────────────────────────────────────────────────────────────────────

    def action_push_chat_screen(self) -> None:
        """Pushes a new chat screen"""

        # Push the logo screen
        self.app.push_screen(ChatScreen())
