# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from typing import Any, TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEXTUAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from textual.app import ComposeResult
from textual.widgets import Static

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from lifegu42d.widgets.chat.chat_input import ChatInput

if TYPE_CHECKING:
    from lifegu42d.utils.classes.chat import Chat


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CHAT WINDOW
# └─────────────────────────────────────────────────────────────────────────────────────


class ChatWindow(Static):
    """A chat window widget"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define default CSS
    DEFAULT_CSS = """
    ChatInput {
        display: none;
    }
    ChatInputMarkdown {
        height: 1fr;
        border: solid #ccc;
        padding: 0 1 0 1;
        overflow-y: scroll;
    }
    ChatOutputMarkdown {
        height: 3fr;
        border: solid green;
        padding: 0 1 0 1;
        overflow-y: scroll;
    }
    """
    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, *args: Any, chat: Chat, **kwargs: Any):
        """Initialize the chat input widget"""

        # Call super init method
        super().__init__(*args, **kwargs)

        # Set chat
        self.chat = chat

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ COMPOSE
    # └─────────────────────────────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        """Compose Method"""

        # Initialize chat input instance
        chat_input = ChatInput("", chat=self.chat, placeholder="Message...")

        # Retrieve chat input markdown instance
        chat_input_markdown = chat_input.input_markdown

        # Register chat output markdown instance
        chat_output_markdown = chat_input.output_markdown

        # Yield markdown and chat input
        yield chat_output_markdown
        yield chat_input_markdown
        yield chat_input
