import openai # type: ignore
import json
from typing import Dict, Any
from constants import *
import yaml
import tiktoken # type: ignore
from grading_context import GradingContext
from criteria import Criterion, Criteria


class LLMHandler:
    """
    LLM handler object interacts with the LLM API calls for the grader.

    Attributes:
        yaml_path: The path of the .yaml file that contains the API key.
    """
    def __init__(self, yaml_path: str, grading_context: GradingContext):
        """
        Initialises a LLMHandler object.

        Args:
            yaml_path: Path to the yaml file which includes the api key.
        """
        with open(yaml_path, 'r') as file:
            config = yaml.safe_load(file)
        
        openai.api_key = config['openai_api_key']
        self.grading_context = grading_context

    def set_criterion(self, criterion: Criterion):
        """
        Set criterion for the LLM Handler to grade the paper again.

        Args:
            criterion: New criterion.
        """
        self.grading_context.criterion = criterion
    
    def create_system_messages(self) -> list[Dict]:
        """
        Creates LLM call messages that include the information regarding marking.

        Args:
            config (dict): The config file for the grader.

        Returns:
            List of dictionaries that contain system message info.
        """
        messages = []

        # Intro message giving context.
        messages.append(
            {
                "role": "system", 
                "content": INTRODUCTION_MESSAGE.format(
                    self.grading_context.config['grade_level']
                    )
            }
        )

    def create_user_messages(self) -> list[Dict]:
        """
        Creates the user messages sent to the LLM API model.

        Returns:
            list of messages to send to the API.
        """
        messages = []
        messages.append(
            {
                "role": "user",
                "content": TASK_PREAMBLE+self.grading_context.task
            }

        )

        messages.append(
            {
                "role": "user", 
                "content": ASSIGNMENT_PREAMBLE+self.grading_context.assignment
            }
        )
        
        messages.append(
            {
                "role": "user",
                "content": (
                    CRITERIA_PREAMBLE + "\n" +
                    "\n".join(f"{i+1}. {c}" for i, c in enumerate(
                        self.grading_context.criterion
                    ))
                )
            }
        )

    def create_messages(self) -> list[Dict]:
        """
        Combines the system and user messages.

        Returns:
            a list of all messages for the LLM API call.
        """
        return self.create_system_messages() + self.create_user_messages()

    def generate_response(self) -> dict:
        """
        Calls the LLM API for the grading process for a singular criterion

        Returns:
            a dictionary of all the data from the API call. Format TBD
        """
        response = openai.ChatCompletion.create(
                model=LLM_MODEL,
                messages=self.create_messages()
            )
        return response