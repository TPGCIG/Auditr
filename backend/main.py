from dotenv import load_dotenv # type: ignore
from openai import OpenAI # type: ignore
import os
from grader import LLM



def main():
    
    load_dotenv()
    os.environ["OPENAI_API_KEY"]

    


    
    
    # client = OpenAI(api_key=config['openai_api_key'])
    
    # assignment_text = """
    # Photosynthesis is the process by which green plants convert sunlight into energy. 
    # It takes in carbon dioxide and water and produces oxygen and glucose.
    # """

    # criteria_text = "Accuracy of scientific explanation about photosynthesis."

    # messages = [
    # {"role": "developer", "content": "You are a strict but fair science teacher grading student answers."},
    # {"role": "user", "content": f"Here is the student's assignment:\n\n{assignment_text}\n\nGrade it based on this criteria: {criteria_text}.\nGive a score (1 = excellent, 2 = good, 3 = needs improvement), and then explain your reasoning."}
    # ]

    # completion = client.chat.completions.create(
    #     model="gpt-4o",  # or "gpt-3.5-turbo" for cheaper calls
    #     messages=messages
    # )

    # # Extract and print the reply
    # print(completion.choices[0].message.content)
    

    
    





if __name__ == "__main__":
    main()










