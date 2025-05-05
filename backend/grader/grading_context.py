from typing import Dict, Any, List
from dataclasses import dataclass
from criteria import Criterion

@dataclass
class GradingContext:
    task: str  # The task sheet/spec
    criterion: Criterion  # List of grading criteria
    assignment: str  # The student's submitted work
    config: Dict  # Any config settings (e.g., model, grade level, etc.)