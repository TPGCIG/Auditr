class GradingError(Exception):
    """Custom error for grading issues."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message