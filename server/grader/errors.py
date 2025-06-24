"""
Java ass file lol
"""

class GradingError(Exception):
    """Custom exception for grading-related issues."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message