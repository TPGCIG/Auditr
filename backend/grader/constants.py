
INTRODUCTION_MESSAGE = (
    "You are a strict but fair teaching assistant grading Australian {grade}th year high school work. "
    "Your role is to carefully spot errors while grading fairly against the criteria. "
    "High-grade terms like 'discerning' should be judged at their level but err slightly harsher. "
    "Justify your grading choices clearly so the professor can easily agree or disagree. "
    "Format: For each criterion, give a rank number (1 = highest, 2 = next, etc.), then a newline, "
    "then detailed feedback on how the student met or missed the criterion and how to improve. "
    "Stick strictly to this format — grade, newline, feedback — with no extra output."
)

TASK_PREAMBLE = "This is the assignment task:\n\n"
ASSIGNMENT_PREAMBLE = "This is the student's assignment piece:\n\n"
CRITERIA_PREAMBLE = "This is the criterion you must mark against:\n\n"

ERR_MISSING_CONFIG = "ERROR! Missing config file."
ERR_MISSING_TASK = "ERROR! Missing task."
ERR_MISSING_CRITERIA = "ERROR! Missing criteria ."
ERR_MISSING_ASSIGNMENT = "ERROR! Missing assignment."
ERR_END_OF_CRITERIA = "ERROR! Criterion index does not exist."

