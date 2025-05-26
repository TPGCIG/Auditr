from openai import OpenAI # type: ignore
from .errors import GenerationError
from .constants import *
import tiktoken # type: ignore


class LLMHandler:
    """
    LLM handler object interacts with the LLM API calls for the grader.

    Attributes:
        api_key (str): The API key 
    """
    def __init__(self, api_key: str):
        """
        Initialises a LLMHandler object.

        Args:
            api_key: The OPENAI api key.
        """
        self._client = OpenAI(api_key=api_key)
        self._user_messages = None
        self._dev_messages = None
    
    def set_developer_messages(self, messages: list[dict]):
        """
        Sets the developer messages for the API call.
        All functions that set messages reset the API response to None.
        
        Parameters:
            messages (list[dict]): The messages.
        """
        self._dev_messages = messages

    def set_user_messages(self, messages: list[dict]):
        """
        Sets the user messages for the API call,
        All functions that set messages reset the API response to None.
        
        Parameters:
            messages (list[dict]): The messages.
        """
        self._user_messages = messages

    def _combine_messages(self) -> list[dict]:
        """
        Returns the full message list for the API call.
        """
        if not self._dev_messages:
            raise GenerationError(ERR_NO_DEV_MSG)
        if not self._user_messages:
            raise GenerationError(ERR_NO_USER_MSG)
        
        return self._dev_messages + self._user_messages

    def generate_response(self):
        """
        Calls the LLM API for the grading process for a singular criterion.
        
        Returns:
            (str) The API response
        """
        if not self._dev_messages:
            raise GenerationError(ERR_NO_DEV_MSG)
        if not self._user_messages:
            raise GenerationError(ERR_NO_USER_MSG)

        response = self._client.chat.completions.create(
                model=LLM_MODEL,
                messages=self._combine_messages()
            )
        
        return response
    
    def get_token_count(self) -> int:
        """
        Gets the token count of a request without sending it.
        Useful for estimating costs.

        Returns:
            Tokens (int)
        """
        encoding = tiktoken.encoding_for_model(LLM_MODEL)
        token_count = 0

        for message in self._combine_messages():
            token_count += len(encoding.encode(message["content"]))

        return token_count