class PromptCloudError(Exception):
    def __init__(self, message: str):
        self.message = message
        self.name = "PromptCloudError"
        super().__init__(self.message)

class PromptNotFoundError(PromptCloudError):
    def __init__(self, message: str):
        self.name = "PromptNotFoundError"
        super().__init__(message)


class ProjectNotSetError(PromptCloudError):
    def __init__(self, message: str):
        self.name = "ProjectNotSetError"
        super().__init__(message)


class PromptCompletionFailedError(PromptCloudError):
    def __init__(self, message: str):
        self.name = "PromptCompletionFailedError"
        super().__init__(message)
