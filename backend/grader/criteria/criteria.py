"""
A criteria is a matrix where:
    Rows represent a standard of work, usually from A, B, C, D, E or different
    Columns represent a category of work that the assignment piece expects 

The row work standard usually only differs by a few key terms which may reduce
 computational costs in asking GPT questions by isolating them.

 Criteria layout for writing is gonna be:
"""
class Criterion:
    def __init__(self, information: list = []):
        self.criterion = information

    def add_level(self, information: str):
        self.criterion.append(information)

class Criteria:
    def __init__(self, grade_level: int = 0):
        self.criteria = []
        self.grade_level = grade_level

    def set_criteria(self, criteria: list[list]):
        self.criteria = criteria

    def get_criteria(self) -> list[Criterion]:
        return self.criteria + ["md:", self.grade_level]

    def add_criterion(self, criterion: list):
        self.criteria.append(criterion)