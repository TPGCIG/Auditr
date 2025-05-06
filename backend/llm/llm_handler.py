from backend.grader.constants import LLM_MODEL
from openai import OpenAI # type: ignore
import json
from typing import Dict, Any
import yaml
import tiktoken # type: ignore


class LLMHandler:
    """
    LLM handler object interacts with the LLM API calls for the grader.

    Attributes:
        yaml_path: The path of the .yaml file that contains the API key.
    """
    def __init__(
        self, api_key: str, developer_messages: list[dict],
        user_messages: list[dict]
    ):
        """
        Initialises a LLMHandler object.

        Args:
            messages: Messages for the api to call with
        """
        
        self.client = OpenAI(api_key)
        self.user_messages = user_messages
        self.dev_messages = developer_messages
    
    def set_developer_messages(self, messages: list[dict]):
        """
        Sets the developer messages for the API call,
        
        Parameters:
            messages (list[dict]): The messages.
        """
        self.dev_messages = messages

    def set_user_messages(self, messages: list[dict]):
        """
        Sets the user messages for the API call,
        
        Parameters:
            messages (list[dict]): The messages.
        """
        self.user_messages = messages

    def _combine_messages(self) -> list[dict]:
        """
        Returns the full message list for the API call.
        """
        return self.set_developer_messages() + self.set_user_messages()

    def _generate_response(self) -> dict:
        """
        Calls the LLM API for the grading process for a singular criterion

        Returns:
            a dictionary of all the data from the API call. Format TBD
        """
        response = self.client.chat.completions.create(
                model=LLM_MODEL,
                messages=self._combine_messages
            )
        return response.choices[0].message.content 
    
    def get_response(self) -> str:
        """
        Gets the response from the API call.

        Returns:
          response.
        """
        return self._generate_response()