import requests
from typing import Optional, List

class PromptCloudClient:
    base_url = "http://acc1-2601-19b-0-e250-847b-4f81-467e-5f7d.ngrok-free.app"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.project_id = None
        self.headers = {
            "x-api-key": self.api_key,
        }

    def fetch_project(self):
        if self.project_id:
            return

        try:
            response = requests.get(f"{self.base_url}/api/projects", headers=self.headers)

            if response.status_code == 200:
                data = response.json()
                self.project_id = data.get('id')
        except Exception as error:
            print(f"Error: {error}")

    def get_prompt(self, name: str) -> Optional[Prompt]:
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
