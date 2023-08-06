import os
import re
import json
import openai
from .error import *
from .schema import *
from typing import Optional, List, Dict, Any


class Prompt:
    """A class representing a Prompt."""

    def __init__(self, id: int, name: str, body: str, description: Optional[str] = None):
        """
        Initialize a new Prompt instance.

        :param id: The unique identifier for the Prompt.
        :param name: The name of the Prompt.
        :param body: The body content of the Prompt.
        :param description: An optional description of the Prompt.
        """
        self.id = id
        self.name = name
        self.body = body
        self.description = description

    def to_json(self) -> str:
        """
        Convert the Prompt instance to a JSON string.

        :return: A string of JSON representing the Prompt instance.
        """
        return json.dumps(self.__dict__)

    @staticmethod
    def create(data: Dict[str, Any]) -> Optional['Prompt']:
        """
        Create a new Prompt instance from a dictionary of attributes.

        :param data: A dictionary containing the attributes for the new Prompt instance.
        :return: A new Prompt instance, or None if the necessary attributes are not present.
        """
        if 'id' in data and 'name' in data and 'body' in data and isinstance(data['id'], int) and \
                isinstance(data['name'], str) and isinstance(data['body'], str):
            return Prompt(data['id'], data['name'], data['body'], data.get('description'))
        else:
            return None

    @staticmethod
    def create_from_list(data_array: List[Dict[str, Any]]) -> List['Prompt']:
        """
        Create a list of Prompt instances from a list of dictionaries.

        :param data_array: A list of dictionaries, each containing the attributes for a new Prompt instance.
        :return: A list of Prompt instances.
        """
        prompts = []

        for data in data_array:
            prompt = Prompt.create(data)
            if prompt:
                prompts.append(prompt)

        return prompts

    def get_placeholders(self) -> List[str]:
        """
        Extract placeholder strings from the Prompt's body content.

        :return: A list of placeholder strings.
        """
        placeholder_pattern = r'\%(.*?)\%'
        matches = re.findall(placeholder_pattern, self.body)

        if not matches:
            return []

        return matches

    def hydrate(self, values: Dict[str, Any]) -> 'Prompt':

        new_body = self.body
        for key, value in values.items():
            re_pattern = r'\%' + re.escape(key) + r'\%'
            new_body = re.sub(re_pattern, str(value), new_body)

        return Prompt(self.id, self.name, new_body, self.description)

    def completion(self, options: CompletionProps):
        """
        Execute a completion request using the OpenAI API.

        :param options: A dictionary containing configuration parameters for the completion request.
        :return: The response from the OpenAI API.
        """
        openai_config = options['config']
        if 'messages' not in openai_config:
            openai_config['messages'] = [
                {
                    "role": "system",
                    "content": self.body,
                }
            ]

        openai_api_key = os.getenv("OPENAI_API_KEY")

        if not openai_api_key:
            raise PromptCloudError(
                "No OpenAI API key is associated with your project. Please add one in the PromptCloud dashboard and try again"
            )

        openai.api_key = openai_api_key

        if 'on_stream_update' in options:
            openai_config['stream'] = True

            buffer = ""

            for chunk in self.generate_response_stream(openai_config):
                buffer += chunk
                options['on_stream_update'](chunk, buffer)

            return buffer

        if 'stream' in openai_config and openai_config['stream']:

            buffer = ""
            for chunk in self.generate_response_stream(openai_config):
                buffer += chunk
                yield chunk

            return buffer

        try:

            openai_response = openai.ChatCompletion.create(**openai_config)
        except Exception as error:
            raise PromptCompletionFailedError(str(error))

        if 'return_raw_response' in options and options['return_raw_response']:
            return openai_response

        if not openai_response['choices']:
            raise PromptCompletionFailedError(
                "No choices available in the OpenAI response")

        return openai_response['choices'][0]['message']['content']

    def generate_response_stream(self, config: OpenAIConfig):
        """
        Execute a streaming completion request using the OpenAI API.

        :param config: A dictionary containing configuration parameters for the completion request.
        """

        for response in openai.ChatCompletion.create(**config):
            res = response['choices'][0].get('delta').get('content')

            if res is None:
                continue

            yield res
