
import yaml
from .errors import GradingError
from constants import *
from grading_context import GradingContext
from ..llm.llm_handler import LLMHandler


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
        self.grading_context = grading_context
        self.llm_handler = llm_handler

    def _create_developer_messages(self) -> list[dict]:
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
                    self.grading_context.config['grade_level']
                    )
            }
        )

        return messages

    def _create_user_messages(self) -> list[dict]:
        """
        Creates the user messages sent to the LLM API model.

        Returns:
            list of messages to send to the API.
        """
        messages = []
        messages.append(
            {
                "role": "user",
                "content": TASK_PREAMBLE+self.grading_context.task
            }

        )

        messages.append(
            {
                "role": "user", 
                "content": ASSIGNMENT_PREAMBLE+self.grading_context.assignment
            }
        )

        messages.append(
            {
                "role": "user",
                "content": (
                    CRITERIA_PREAMBLE + "\n" +
                    "\n".join(f"{i+1}. {c}" for i, c in enumerate(
                        self.grading_context.criteria[self.criterion_index]
                    ))
                )
            }
        )
        return messages

    def _create_messages(self) -> list[dict]:
        """
        Combines the system and user messages.

        Returns:
            a list of all messages for the LLM API call.
        """
        return self.create_system_messages() + self.create_user_messages()

    def grade_paper(self):
        """
        Grades the paper. Grader must be equipped with the task details, 
        criteria, final piece and a config before it can grade.
        
        Does not return the grade results. Refer to get_grading
        """
        if not self.grading_context.task:
            raise GradingError(ERR_MISSING_TASK)
        elif not self.grading_context.criteria:
            raise GradingError(ERR_MISSING_CRITERIA)
        elif not self.grading_context.config:
            raise GradingError(ERR_MISSING_CONFIG)
        elif not self.grading_context.assignment:
            raise GradingError(ERR_MISSING_ASSIGNMENT)
        
        #TODO Use parameters for cyclic LLM calls.

        responses = []
        
        # Set up a while loop that does the calls for the API but breaks
        # after 10 calls no matter what in case the loop isnt broken out of.
        failsafe_count = 0
        self.llm_handler.set_developer_messages(self._create_developer_messages())

        while failsafe_count <= 9:
            self.llm_handler.set_user_messages(self._create_user_messages())
            responses.append(self.llm_handler.get_response())

            if self.grading_context.criteria.index_criterion(): 
                break  

            failsafe_count += 1

        return responses
    

    def get_grading(self) -> list:
        return self.results