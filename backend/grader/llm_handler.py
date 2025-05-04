import openai
import json
from typing import Dict, Any

MODEL = "gpt-4o"


def create_llm_messages(config: Dict[Any]) -> list[Dict]:



def grade_paper(text: String, criteria: Criteria)
"""
    Grades the given text against criteria given through cyclicly asking
    through each criteria standard.

    Args:
        text (str): The student's paper text.
        criteria (Criteria): The teacher's grading criteria.

    Returns:
        str: The grade and feedback.
    """

    prompt = f"""
You are a grading assistant. Grade the following student paper based on these criteria:

Criteria:
{criteria}

Student's paper:
{text}

Provide a grade and brief feedback.
"""

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a strict but fair grading assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content'].strip()
