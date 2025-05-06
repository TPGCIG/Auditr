
class Criterion:
    def __init__(self, information: list = []):
        self.criterion = information

    def add_level(self, information: str):
        self.criterion.append(information)

class Criteria:
    """
    A criteria is a matrix where:
        Rows represent a standard of work, usually from A, B, C, D, E or different
        Columns represent a category of work that the assignment piece expects 

    The row work standard usually only differs by a few key terms which may reduce
    computational costs in asking GPT questions by isolating them.

    Criteria layout for writing is gonna be:
    """
    def __init__(self, grade_level: int = 0):
        self.criteria = []
        self.grade_level = grade_level
        self.current_criterion = 0;
    
    def index_criterion(self):
        """

        Indexes the current criterion to the next.

        Returns 1 if there is no following one.
        """
        if (self.current_criterion + 1 >= len(self.criteria)):
            return 1
        self.criterion_index += 1
        return 0

    def set_criteria(self, criteria: list[list]):
        self.criteria = criteria

    def get_criteria(self) -> list[Criterion]:
        return self.criteria + ["md:", self.grade_level]

    def add_criterion(self, criterion: list):
        self.criteria.append(criterion)

    def get_current_criterion(self):
        return self.criteria[self.current_criterion]