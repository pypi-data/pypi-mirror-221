import json
import re
from typing import Optional, List, Dict, Any

class Prompt:
    def __init__(self, id: int, name: str, body: str, description: Optional[str] = None):
        self.id = id
        self.name = name
        self.body = body
        self.description = description

    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    @staticmethod
    def create(data: Dict[str, Any]) -> Optional['Prompt']:
        if 'id' in data and 'name' in data and 'body' in data and isinstance(data['id'], int) and \
                isinstance(data['name'], str) and isinstance(data['body'], str):
            return Prompt(data['id'], data['name'], data['body'], data.get('description'))
        else:
            return None

    @staticmethod
    def create_from_list(data_array: List[Dict[str, Any]]) -> List['Prompt']:
        prompts = []

        for data in data_array:
            prompt = Prompt.create(data)
            if prompt:
                prompts.append(prompt)

        return prompts

    def get_placeholders(self) -> List[str]:
        placeholder_pattern = r'\{(.*?)\}'
        matches = re.findall(placeholder_pattern, self.body)

        if not matches:
            return []

        return matches

    def hydrate(self, values: Dict[str, Any]) -> str:
        hydrated_body = self.body

        for key, value in values.items():
            re_pattern = r'\{' + re.escape(key) + r'\}'
            hydrated_body = re.sub(re_pattern, str(value), hydrated_body)

        return hydrated_body
