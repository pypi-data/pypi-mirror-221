# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

from textual import on
from textual.binding import Binding
from textual.widgets import Input
from typing import Any, TYPE_CHECKING

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from lifegu42d.widgets.chat.chat_input_markdown import ChatInputMarkdown
from lifegu42d.widgets.chat.chat_output_markdown import ChatOutputMarkdown

if TYPE_CHECKING:
    from lifegu42d.utils.classes.chat import Chat


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CHAT INPUT
# └─────────────────────────────────────────────────────────────────────────────────────


class ChatInput(Input):
    """A chat input widget"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Set bindings
    BINDINGS = Input.BINDINGS + [
        Binding("ctrl+n", "cursor_new_line", "cursor new line", show=False),
    ]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, *args: Any, chat: Chat, **kwargs: Any):
        """Initialize the chat input widget"""

        # Call super init method
        super().__init__(*args, **kwargs)

        # Set chat
        self.chat = chat

        # Initialize and set input markdown
        self.input_markdown = ChatInputMarkdown("|")

        # Initialize and set output markdown
        self.output_markdown = ChatOutputMarkdown()
        self.output_markdown_text = ""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ UPDATE CURSOR
    # └─────────────────────────────────────────────────────────────────────────────────

    def update_cursor(self) -> None:
        """Updates the cursor in the markdown"""

        # Update cursor in markdown
        self.input_markdown.update(
            self.value[: self.cursor_position]
            + "|"
            + self.value[self.cursor_position :]  # noqa
        )

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ UPDATE OUTPUT MARKDOWN
    # └─────────────────────────────────────────────────────────────────────────────────

    @on(Input.Changed)
    def update_input_markdown(self, event: Input.Changed) -> None:
        """Updates the input markdown value with the input value"""

        # Update cursor
        self.update_cursor()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ UPDATE OUTPUT MARKDOWN
    # └─────────────────────────────────────────────────────────────────────────────────

    @on(Input.Submitted)
    async def update_output_markdown(self, event: Input.Submitted) -> None:
        """Updates the output markdown value with the input value"""

        # Return if input value is empty
        if not self.value:
            return
        # Get message
        message = self.value

        # Clear input value
        self.value = ""

        # Set cursor position
        self.cursor_position = 0

        # Update cursor
        self.update_cursor()

        # Update output markdown text
        self.output_markdown_text += "\n\n**User:**\n\n" + message

        # Update output markdown text
        self.output_markdown_text += "\n\n**ChatGPT:**\n\n"

        # Update output markdown
        self.output_markdown.update(self.output_markdown_text)
        self.output_markdown.scroll_end()

        # Initialize count
        count = 0
        n_responses = 5

        # Iterate over responses
        async for response in self.chat.send(message):
            # Update output markdown text
            self.output_markdown_text += response

            # Check if should update
            if count == 0 or count % n_responses == 0:
                # Update output markdown
                self.output_markdown.update(self.output_markdown_text)
                self.output_markdown.scroll_end()

            # Increment count
            count += 1

        # Update output markdown
        self.output_markdown.update(self.output_markdown_text)
        self.output_markdown.scroll_end()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ ACTION CURSOR LEFT
    # └─────────────────────────────────────────────────────────────────────────────────

    def action_cursor_left(self) -> None:
        """Cursor left action"""

        # Call super action method
        super().action_cursor_left()

        # Update cursor
        self.update_cursor()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ ACTION CURSOR NEW LINE
    # └─────────────────────────────────────────────────────────────────────────────────

    def action_cursor_new_line(self) -> None:
        """Cursor new line action"""

        # Set input value
        self.value += "\n\n"

        # Update cursor position
        self.cursor_position = len(self.value)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ ACTION CURSOR RIGHT
    # └─────────────────────────────────────────────────────────────────────────────────

    def action_cursor_right(self) -> None:
        """Cursor right action"""

        # Call super action method
        super().action_cursor_right()

        # Update cursor
        self.update_cursor()
