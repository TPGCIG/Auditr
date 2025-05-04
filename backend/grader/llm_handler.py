import openai # type: ignore
import json
from typing import Dict, Any
from constants import *
import yaml
import tiktoken # type: ignore


class LLMHandler:
    """
    LLM handler object interacts with the LLM API calls for the grader.

    Attributes:
        yaml_path: The path of the .yaml file that contains the API key.
    """
    def __init__(self, yaml_path: str):
        """
        Initialises a LLMHandler object.

        Args:
            yaml_path: Path to the yaml file which includes the api key.
        """
        with open(yaml_path, 'r') as file:
            config = yaml.safe_load(file)
        
        openai.api_key = config['openai_api_key']


    
    

    def create_system_messages(config: Dict[Any]) -> list[Dict]:
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
                "content": INTRODUCTION_MESSAGE.format(config)
            }
        )
        
    
    
    
response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a strict but fair grading assistant."},
                #{"role": "user", "content": prompt}
            ]
        )


