from typing import Dict, Any, List
from dataclasses import dataclass
from .criteria.criteria import Criteria

@dataclass
class GradingContext:
    """
    Data type containing all information regarding grading.

    Arguments:
        task (str): The task details of the assignment written.
        criteria (Criteria): The task's criteria.
        assignment (str): The assignment written by the student.
        config (dict): A config file for info regarding the grader.
    """
    task: str  # The task sheet/spec
    criteria: Criteria  # List of grading criteria
    assignment: str  # The student's submitted work
    config: Dict  # Any config settings (e.g., model, grade level, etc.)