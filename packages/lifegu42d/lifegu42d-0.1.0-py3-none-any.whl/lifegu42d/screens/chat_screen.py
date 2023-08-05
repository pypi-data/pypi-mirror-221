# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from typing import Any

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEXTUAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from textual import work
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import LoadingIndicator

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ PROJECT IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from lifegu42d.utils.classes.chat import Chat
from lifegu42d.widgets.chat.chat_auth_form import ChatAuthForm
from lifegu42d.widgets.chat.chat_window import ChatWindow


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CHAT AUTH SCREEN
# └─────────────────────────────────────────────────────────────────────────────────────


class ChatAuthScreen(Screen[Any]):
    """A chat authentication screen for the LIFEGU42D application"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define bindings
    BINDINGS = []

    # Define default CSS
    DEFAULT_CSS = """
    """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, *args: Any, chat: Chat, **kwargs: Any):
        """Init Method"""

        # Call super init method
        super().__init__(*args, **kwargs)

        # Set chat
        self.chat = chat

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ COMPOSE
    # └─────────────────────────────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        """Compose Method"""

        # Yield loading indicator
        yield LoadingIndicator()

        # Yield chat auth form
        yield ChatAuthForm()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ ON MOUNT
    # └─────────────────────────────────────────────────────────────────────────────────

    def on_mount(self) -> None:
        """On Mount Method"""

        # Get loading indicator and set display to False
        loading_indicator = self.query_one(LoadingIndicator)
        loading_indicator.display = False

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ AUTHENTICATE
    # └─────────────────────────────────────────────────────────────────────────────────

    @work
    async def authenticate(self, api_key: str) -> None:
        """Authenticates the chat instance"""

        # Assert that app has update config method
        assert hasattr(self.app, "update_config")

        # Set API key
        self.chat.set_credentials(api_key=api_key)

        # Get chat auth form and set display to False
        chat_auth_form = self.query_one(ChatAuthForm)
        chat_auth_form.display = False

        # Get loading indicator and set display to True
        loading_indicator = self.query_one(LoadingIndicator)
        loading_indicator.display = True

        # Authenticate chat
        await self.chat.authenticate()

        # Check if chat is authenticated
        if self.chat.is_authenticated:
            # Update app config
            self.app.update_config(api_key=api_key)

            # Pop screen
            self.app.pop_screen()

        # Set loading indicator display to False
        loading_indicator.display = False

        # Set chat auth form display to True
        chat_auth_form.display = True


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CHAT SCREEN
# └─────────────────────────────────────────────────────────────────────────────────────


class ChatScreen(Screen[Any]):
    """A chat screen for the LIFEGU42D application"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Define bindings
    BINDINGS = []

    # Define default CSS
    DEFAULT_CSS = """
    """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Init Method"""

        # Call super init method
        super().__init__(*args, **kwargs)

        # Assert that app has config
        assert hasattr(self.app, "config") and isinstance(self.app.config, dict)

        # Get config
        config = self.app.config

        # Get API key
        api_key = config.get("api_key", "")

        # Initialize chat instance
        self.chat = Chat(api_key=api_key)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ COMPOSE
    # └─────────────────────────────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        """Compose Method"""

        # Yield loading indicator
        yield LoadingIndicator()

        # Yield chat window
        yield ChatWindow(chat=self.chat)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ ON MOUNT
    # └─────────────────────────────────────────────────────────────────────────────────

    def on_mount(self) -> None:
        """On Mount Method"""

        # Get chat window and set display to False
        chat_window = self.query_one(ChatWindow)
        chat_window.display = False

        # Authenticate chat
        self.authenticate()

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ AUTHENTICATE
    # └─────────────────────────────────────────────────────────────────────────────────

    @work
    async def authenticate(self) -> None:
        """Authenticates the chat instance"""

        # Authenticate chat
        await self.chat.authenticate()

        # Get loading indicator and set display to False
        loading_indicator = self.query_one(LoadingIndicator)
        loading_indicator.display = False

        # Check if chat is not authenticated
        if not self.chat.is_authenticated:
            # Push auth screen
            self.app.push_screen(ChatAuthScreen(chat=self.chat))

        # Set chat window display to True
        chat_window = self.query_one(ChatWindow)
        chat_window.display = True
