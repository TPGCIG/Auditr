import openai
import yaml

def load_api_keys():
    with open('../config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

config = load_api_keys()

openai.api_key = config['openai_api_key']

def grade_paper(text, criteria):
    """
    Grades the given text (e.g., OCR result) against user criteria.

    Args:
        text (str): The student's paper text.
        criteria (str): The teacher's grading criteria.

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
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a strict but fair grading assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content'].strip()
