import openai # type: ignore
import yaml
from .errors import GradingError
from constants import *
from grading_context import GradingContext

class Grader:
    """
    A grading assistant that grades student papers based on given criteria.

    Attributes:
        task_details (str): the task that the student's piece is written to.
        criteria (Criteria): the criteria that the student is being graded 
            against.
        final_piece (str): the paper by the student that is getting graded.
        config (dict): the configuration of the grader.     
    """

    def __init__(self, grading_context: GradingContext):
        """
        Initialises a Grader that grades student papers based on a given 
        criteria.

        Args:
            task_details (str): the task that the student's piece is written to.
            criteria (Criteria): the criteria that the student is being graded 
                against.
            final_piece (str): the paper by the student that is getting graded.
            config (dict): the configuration of the grader.
        """
        self.task = grading_context.task
        self.criteria = grading_context.criteria
        self.assignment = grading_context.assignment
        self.config = grading_context.config
        self.results = {}



    def grade_paper(self):
        """
        Grades the paper. Grader must be equipped with the task details, 
        criteria, final piece and a config before it can grade.
        
        Does not return the grade results. Refer to get_grading
        """
        if not self.task_details:
            raise GradingError(ERR_MISSING_TASK)
        elif not self.criteria:
            raise GradingError(ERR_MISSING_CRITERIA)
        elif not self.config:
            raise GradingError(ERR_MISSING_CONFIG)
        elif not self.final_piece:
            raise GradingError(ERR_MISSING_ASSIGNMENT)
        
        #TODO Use parameters for cyclic LLM calls.







        #return response['choices'][0]['message']['content'].strip()
    

    def get_grading(self) -> list:
        pass