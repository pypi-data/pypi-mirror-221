# PromptCloud Python SDK

The PromptCloud Python SDK provides a seamless and easy way to interact with the PromptCloud API. It simplifies the process of making requests and handling responses from the API.

## Features

The SDK offers the following features:

- Fetching project information
- Fetching a specific prompt by name
- Fetching all prompts for a specific project
- Executing a completion request using the OpenAI API
- Streaming updates during a completion request
- Handling custom errors

## Installation

You can install the PromptCloud Python SDK via pip:

```bash
pip install promptcloud_sdk
```

## Usage

### Importing the Client

Firstly, import the `PromptCloudClient` from the SDK.

```python
from promptcloud_sdk.client import PromptCloudClient
```

### Instantiating the Client

Then, instantiate a new `PromptCloudClient` object using your API key.

```python
client = PromptCloudClient("<YOUR_API_KEY>")
```

### Fetching Project Information

Call the `fetch_project` method to retrieve project information from the PromptCloud API.

```python
client.fetch_project()
```

### Fetching a Specific Prompt

Use the `get_prompt` method and specify the prompt name to retrieve a specific prompt.

```python
prompt = client.get_prompt("<PROMPT_NAME>")
```

### Fetching All Prompts for a Project

Call the `list_prompts` method to retrieve all prompts for a specific project.

```python
prompts = client.list_prompts()
```

### Executing a Completion Request

Here is an example of executing a completion request:

```python
options = {
    'config': {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'user',
                'content': 'Translate the following English text to French: "{text}"'
            }
        ],
    }
}

response = prompt.completion(options)
```

### Streaming Updates during a Completion Request

The SDK also supports streaming updates during a completion request. Here is an example:

```python
def update(chunk_value: str, current_completion: str):
    print(chunk_value)

options = {
    'config': {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'user',
                'content': 'Translate the following English text to French: "{text}"'
            }
        ],
        'stream': True
    },
    'on_stream_update': update
}

response = prompt.completion(options)
```

## Documentation

For more in-depth documentation, refer to the following sections.

### Methods

#### `fetch_project()`

Fetches project information from the PromptCloud API.

#### `get_prompt(name: str) -> Optional[Prompt]`

Fetches a specific prompt by name from the PromptCloud API.

#### `list_prompts() -> Optional[List[Prompt]]`

Fetches all prompts for a specific project from the PromptCloud API.

#### `completion(options: CompletionProps)`

Executes a completion request using the OpenAI API. The `options` parameter should be a dictionary in the format specified by the `CompletionProps` class. 

#### `hydrate(values: Dict[str, Any]) -> 'Prompt'`

Replaces placeholders in the prompt body with provided values. Placeholders in the text should be in the format `%<placeholder>%`. The `values` parameter should be a dictionary where keys are placeholder names and values are the replacements. Returns a new instance of `Prompt` with the updated body.

#### `get_placeholders() -> List[str]`

Extracts placeholder strings from the Prompt's body content. Returns a list of placeholder strings.

#### `create_from_list(data_array: List[Dict[str, Any]]) -> List['Prompt']`

Creates a list of Prompt instances from a list of dictionaries, each containing the attributes for a new Prompt instance. Returns a list of Prompt instances.

#### `create(data: Dict[str, Any]) -> Optional['Prompt']`

Creates a new Prompt instance from a dictionary of attributes. Returns a new Prompt instance, or None if the necessary attributes are not present.

#### `to_json() -> str`

Converts the Prompt instance to a JSON string. Returns a string of JSON representing the Prompt instance.

### Example

Here is an example of using the `hydrate` method:

```python
# Get a specific prompt
prompt = client.get_prompt("<PROMPT_NAME>")

# Hydrate the prompt
values = {'placeholder1': 'value1', 'placeholder2': 'value2'}
hydrated_prompt = prompt.hydrate(values)
```

In this example, the text of the prompt would have placeholders (e.g., `%placeholder1%`, `%placeholder2%`) replaced with the corresponding values provided in the `values` dictionary. The `hydrate` method returns a new `Prompt` instance with the updated body text.


### Classes

#### `Prompt`

A class that represents a prompt.

#### `PromptCloudClient`

A client class that is used to interact with the PromptCloud API.

### Errors

#### `PromptCloudError`

The base class for all custom errors in the SDK.

#### `PromptNotFoundError`

Thrown when a requested prompt is not found.

#### `ProjectNotSetError`

Thrown when the project ID is not set.

#### `PromptCompletionFailedError`

Thrown when a prompt completion request fails.

### Types

#### `StreamUpdateFunction`

A callable that receives a chunk of the completion text and the total text completed so far.

#### `OpenAIConfig`

A dictionary representing the configuration parameters for a completion request.

#### `CompletionProps`

A dictionary representing the properties of a completion request.

## Contributing

We welcome contributions! If you wish to contribute, please check out our contributing guidelines and our code of conduct for more information.

## License

The PromptCloud Python SDK is licensed under the MIT License.