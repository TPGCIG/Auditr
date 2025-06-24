from dataclasses import dataclass
from .criteria.criteria import Criteria
from typing import List

@dataclass
class GradedResult:
    user_id: int
    assignemnt_name: str
    criteria_results: List[int]
    overall_grade: int