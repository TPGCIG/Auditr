import yaml
from .errors import GradingError
from .constants import *
from .grading_context import GradingContext
from llm.llm_handler import LLMHandler

class Grader:
    """
    A grading assistant that grades student papers based on given criteria.

    Attributes:
        grading_context (GradingContext): GradingContext including all info.
        llm_handler (LLMHandler): A LLM handler for API calls.   
    """
    def __init__(self, grading_context: GradingContext, llm_handler: LLMHandler):
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
        self._grading_context = grading_context
        self._llm_handler = llm_handler

    def _create_developer_messages(self) -> list[dict[str, str]]:
        """
        Creates LLM call messages that include the information regarding marking.

        Args:
            config (dict): The config file for the grader.

        Returns:
            List of dictionaries that contain developer message info.
        """
        messages = []

        # Intro message giving context.
        messages.append(
            {
                "role": "developer", 
                "content": INTRODUCTION_MESSAGE.format(
                    self._grading_context.config['grade_level']
                    )
            }
        )
        return messages

    def _create_user_messages(self, criterion: list[str]) -> list[dict]:
        """
        Creates the user messages sent to the LLM API model.
        
        Arguments:
            criterion (list[str]): The current criterion

        Returns:
            list of messages to send to the API.
        """
        messages = []
        messages.append(
            {
                "role": "user",
                "content": TASK_PREAMBLE+self._grading_context.task
            }

        )

        messages.append(
            {
                "role": "user", 
                "content": ASSIGNMENT_PREAMBLE+self._grading_context.assignment
            }
        )

        messages.append(
            {
                "role": "user",
                "content": (
                    CRITERIA_PREAMBLE + "\n" +
                    "\n".join(f"{i+1}. {c}" for i, c in enumerate(criterion))
                )
            }
        )
        return messages
    

    def grade_paper(self):
        """
        Grades the paper. Grader must be equipped with the task details, 
        criteria, final piece and a config before it can grade.
        
        Returns grading responses
        """
        if not self._grading_context.task:
            raise GradingError(ERR_MISSING_TASK)
        elif not self._grading_context.criteria:
            raise GradingError(ERR_MISSING_CRITERIA)
        elif not self._grading_context.config:
            raise GradingError(ERR_MISSING_CONFIG)
        elif not self._grading_context.assignment:
            raise GradingError(ERR_MISSING_ASSIGNMENT)

        responses = []
        
        # Set up a while loop that does the calls for the API but breaks
        # after 10 calls no matter what in case the loop isnt broken out of.
        failsafe_count = 0
        self._llm_handler.set_developer_messages(self._create_developer_messages())

        # In a loop, generate the grading for each criterion.
        for criterion in self._grading_context.criteria:
            # Sets the LLM's new criterion and generates the solution.
            self._llm_handler.set_user_messages(self._create_user_messages(criterion))
            responses.append(self._llm_handler.generate_response())
            
            # Failsafe to check that the function doesnt loop more than needed
            failsafe_count += 1
            if failsafe_count >= 9:
                break

        return responses