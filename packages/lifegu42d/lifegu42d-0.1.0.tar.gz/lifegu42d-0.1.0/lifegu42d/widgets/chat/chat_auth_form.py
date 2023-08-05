# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Any

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEXTUAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from textual import on
from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Button, Static


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from lifegu42d.widgets.input.labelled_input import LabelledInput


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CHAT AUTH FORM
# └─────────────────────────────────────────────────────────────────────────────────────


class ChatAuthForm(Container):
    """A chat authentication form for the LIFEGU42D application"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define default CSS
    DEFAULT_CSS = """
    ChatAuthForm {
        height: auto;
    }
    """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, *args: Any, **kwargs: Any):
        """Init Method"""

        # Call super init method
        super().__init__(*args, **kwargs)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ COMPOSE
    # └─────────────────────────────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        """Compose Method"""

        # Initialize, set, and yield API key labelled input
        self.api_key_labelled_input = LabelledInput("OpenAI API Key")
        yield self.api_key_labelled_input

        # Yield save button
        yield Button("Save", variant="primary", id="save")
        yield Static("https://platform.openai.com/signup")

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ SAVE
    # └─────────────────────────────────────────────────────────────────────────────────

    @on(Button.Pressed, "#save")
    def save(self) -> None:
        """Saves the API key and closes the auth form"""

        # Get API key
        api_key_labelled_input = self.api_key_labelled_input
        api_key = api_key_labelled_input.input.value

        # Return if API key is empty
        if not api_key:
            return

        # Assery screen has authenticated method
        assert hasattr(self.screen, "authenticate")

        # Authenticate chat
        self.screen.authenticate(api_key=api_key)
