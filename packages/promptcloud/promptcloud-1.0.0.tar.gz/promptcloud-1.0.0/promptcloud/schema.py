from typing import TypedDict, List, Dict, Any, Callable

class StreamUpdateFunction(TypedDict, total=False):
    chunk_value: str
    current_completion: str

class OpenAIConfig(TypedDict, total=False):
    model: str
    messages: List[Dict[str, Any]]
    temperature: float
    top_p: float
    frequency_penalty: float
    presence_penalty: float
    max_tokens: int
    n: int
    stream: bool

class CompletionProps(TypedDict, total=False):
    config: OpenAIConfig
    return_raw_response: bool
    on_stream_update: Callable[[StreamUpdateFunction], None]