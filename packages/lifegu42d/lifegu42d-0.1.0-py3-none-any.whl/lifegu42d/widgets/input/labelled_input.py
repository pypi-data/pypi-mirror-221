# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from typing import Any

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEXTUAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Input, Label


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ LABELLED INPUT
# └─────────────────────────────────────────────────────────────────────────────────────


class LabelledInput(Widget):
    """A labelled input widget"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of label
    label: Label

    # Declare type of input
    input: Input

    # Define default CSS
    DEFAULT_CSS = """
    LabelledInput {
            width: 80%;
            margin: 1;
    }
    LabelledInput {
            layout: horizontal;
            height: auto;
    }
    LabelledInput Label {
            padding: 1;
            width: 12;
            text-align: right;
    }
    LabelledInput Input {
            width: 1fr;
    }
    """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, input_label: str, *args: Any, **kwargs: Any) -> None:
        """Init Method"""

        # Set input label
        self.input_label = input_label

        # Call super init
        super().__init__(*args, **kwargs)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ COMPOSE
    # └─────────────────────────────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        """Compose Method"""

        # Initialize, set, and yield label
        self.label = Label(self.input_label)
        yield self.label

        # Initialize, set, and yield input
        self.input = Input()
        yield self.input
