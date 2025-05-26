from dotenv import load_dotenv # type: ignore
from openai import OpenAI # type: ignore
import os
from grader.grader import Grader
from llm.llm_handler import LLMHandler
from flask import Flask
from flask_cors import CORS
from flask_app.routes import upload_bp

app = Flask(__name__)
CORS(app)


def main():
    
    load_dotenv()
    os.environ["OPENAI_API_KEY"]

    



    
    





if __name__ == "__main__":
    app.run(debug=True, port=5000)
    main()










