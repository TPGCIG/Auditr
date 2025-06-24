class Criteria:
    """
    A criteria is a matrix where:
        Rows represent a standard of work, usually from A, B, C, D, E or 
        different
        
        Columns represent a category of work that the assignment piece expects 

    The row work standard usually only differs by a few key terms which may reduce
    computational costs in asking GPT questions by isolating them.

    POTENTIAL IMPROVEMENT!??!111!! TODO fix

    Criteria layout for writing is gonna be 2d matrix where:
        Top level list is a list of criteria n long - 0 is highest, n lowest. 
        Low level list is a list of criterion expectations - unordered.

    Java ass file lmfao
    """
    def __init__(self, grade_level: int | None = None):
        self.criteria = []
        self.grade_level = grade_level
        self.current_criterion = 0;
    
    def __iter__(self):
        """
        Resets and returns the iterator (self).
        """
        self._current_index = 0
        return self
    
    def __next__(self):
        """
        Returns the next criterion in iteration.
        """
        if self._current_index >= len(self.criteria):
            raise StopIteration
        criterion = self.criteria[self._current_index]
        self._current_index += 1
        return criterion

    def set_criteria(self, criteria: list[list[str]]):
        """
        Sets the criteria fully:

        Parameters:
            criteria (list[list]): the full 2d matrix.
        """
        self.criteria = criteria

    def get_criteria(self) -> list[list[str]]:
        """
        Gets the criteria.

        Returns:
            The criteria in a 2d matrix.
        """
        return self.criteria

    def add_criterion(self, criterion: list[str]):
        """
        Adds a criterion to the right side of the criteria.

        Parameters:
            criterion (list[str]): A criterion as an array.
        """
        self.criteria.append(criterion)

    def get_current_criterion(self):
        """
        Gets the current criterion based on the index.

        Returns:
            The criterion list.
        """
        if not self.criteria:
            return None
        return self.criteria[self._current_index]