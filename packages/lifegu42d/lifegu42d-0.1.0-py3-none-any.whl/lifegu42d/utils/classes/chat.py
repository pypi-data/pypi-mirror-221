# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import openai

from typing import AsyncGenerator


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CHAT
# └─────────────────────────────────────────────────────────────────────────────────────


class Chat:
    """A utility class for a chat session"""

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Declare type of models
    models: None | tuple[str, ...]

    # Declare type of messages
    messages: list[dict[str, str]]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ __INIT__
    # └─────────────────────────────────────────────────────────────────────────────────

    def __init__(self, api_key: str = "", api_secret: str = "") -> None:
        """Init Method"""

        # Set the API key and secret
        self.api_key = api_key

        # Set is authenticated to False
        self.is_authenticated = False

        # Initialize models
        self.models = None

        # Initialize messages
        self.messages = [
            {
                "role": "system",
                "content": (
                    "You are here to assist the user to learn "
                    "the C programming language from scratch."
                    "Ensure all of your responses are markdown-compatible."
                ),
            },
        ]

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ HAS CREDENTIALS
    # └─────────────────────────────────────────────────────────────────────────────────

    @property
    def has_credentials(self) -> bool:
        """Returns a boolean of whether the API key and secret are defined"""

        # Return True if the API key is defined
        return bool(self.api_key)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ AUTHENTICATE
    # └─────────────────────────────────────────────────────────────────────────────────

    async def authenticate(self) -> None:
        """Authenticates the chat session"""

        # Set is authenticated to False
        self.is_authenticated = False

        # Get the API key and secret
        api_key = self.api_key

        # Initialize try-except block
        try:
            # Get models from OpenAI
            response_json = await openai.Model.alist(api_key=api_key)  # type: ignore

        # Handle AuthenticationError
        except openai.error.AuthenticationError:
            # Set API key to empty string
            self.api_key = ""

        # Handle successful authentication
        else:
            # Set models
            self.models = tuple(
                [
                    model["id"]
                    for model in response_json["data"]
                    if model["object"] == "model"
                ]
            )

            # Set is authenticated to True
            self.is_authenticated = True

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ SET CREDENTIALS
    # └─────────────────────────────────────────────────────────────────────────────────

    def set_credentials(self, api_key: str) -> None:
        """Sets the API key and secret"""

        # Set the API key and secret
        self.api_key = api_key

        # Set is authenticated to False
        self.is_authenticated = False

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ SEND
    # └─────────────────────────────────────────────────────────────────────────────────

    async def send(self, message: str) -> AsyncGenerator[str, None]:
        """Sends a message to the chat session"""

        # Get messages
        messages = self.messages + [{"role": "user", "content": message}]

        # Make API request
        responses = await openai.ChatCompletion.acreate(
            model=self.models[-1] if self.models else "gpt-3.5-turbo",
            messages=messages,
            api_key=self.api_key,
            stream=True,
        )  # type: ignore

        # Initialize response key
        response_key = "delta"

        # Check if responses is a dictionary
        if isinstance(responses, dict):
            # Ensure that responses is a list
            responses = [responses]

            # Set key to response
            response_key = "message"

        # Initialize response content
        response_content = ""

        # Initialize is first response to True
        is_first_response = True

        # Iterate over responses
        async for response in responses:
            # Get choices
            choices = response["choices"]

            # Get choice
            choice = choices[0]

            # Get choice response
            choice_response = choice[response_key]

            # Continue if content not in choice response
            if "content" not in choice_response:
                continue

            # Extract response text
            response_text = choice_response["content"]

            # Check if is first response
            if is_first_response:
                # Left strip response text
                response_text = response_text.lstrip()

                # Set messages
                self.messages = messages

            # Yield response text
            yield response_text

            # Add to response content
            response_content += response_text

            # Set is first response to False
            is_first_response = False

        # Append response to messages
        self.messages.append({"role": "assistant", "content": response_content})
