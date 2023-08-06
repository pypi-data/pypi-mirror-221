import os
import requests
from typing import Optional, List
from .prompt import Prompt

class PromptCloudClient:
    """A client to interact with the PromptCloud API."""
    
    base_url = "https://promptcloud-dde2335146b0.herokuapp.com"

    def __init__(self, api_key: str):
        """
        Initialize a new PromptCloudClient instance.

        :param api_key: The API key for the PromptCloud API.
        """
        self.api_key = api_key
        self.project_id = None
        self.headers = {
            "x-api-key": self.api_key,
        }

    def fetch_project(self):
        """
        Fetch project information from the PromptCloud API.
        """
        if self.project_id:
            return

        try:
            response = requests.get(f"{self.base_url}/api/projects", headers=self.headers)

            if response.status_code == 200:
                data = response.json()
                self.project_id = data.get('id')
                
                os.environ["OPENAI_API_KEY"] = data.get('openai_api_key', None)

        except Exception as error:
            print(f"Error: {error}")

    def get_prompt(self, name: str) -> Optional[Prompt]:
        """
        Fetch a specific Prompt from the PromptCloud API.

        :param name: The name of the Prompt to fetch.
        :return: The fetched Prompt instance, or None if the Prompt could not be fetched.
        """
        self.fetch_project()

        if not self.project_id:
            print("Project ID is not set")
            return None

        try:
            response = requests.get(
                f"{self.base_url}/api/prompts/name/{name}", headers=self.headers)

            if response.status_code == 200:
                data = response.json()

                prompt = Prompt.create(data)

                return prompt
        except Exception as error:
            print(f"Error: {error}")
            return None

    def list_prompts(self) -> Optional[List[Prompt]]:
        """
        Fetch a list of all Prompts from the PromptCloud API.

        :return: A list of Prompt instances, or None if the Prompts could not be fetched.
        """
        self.fetch_project()

        if not self.project_id:
            print("Project ID is not set")
            return None

        try:
            response = requests.get(
                f"{self.base_url}/api/projects/{self.project_id}/prompts", headers=self.headers)

            if response.status_code == 200:
                data = response.json()

                prompts = Prompt.create_from_list(data)

                return prompts
        except Exception as error:
            print(f"Error: {error}")
            return None
