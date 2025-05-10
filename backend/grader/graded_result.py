from dataclasses import dataclass
from .criteria.criteria import Criteria


@dataclass
class GradedResult:
    user_id: int
    assignemnt_name: str
    criteria_results: list[Criteria, list[int]]
    overall_grade: int