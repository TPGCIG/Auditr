from typing import Dict, Any, List
from dataclasses import dataclass
from criteria import Criterion, Criteria

@dataclass
class GradingContext:
    task: str  # The task sheet/spec
    criteria: Criteria  # List of grading criteria
    current_criterion: Criterion
    assignment: str  # The student's submitted work
    config: Dict  # Any config settings (e.g., model, grade level, etc.)