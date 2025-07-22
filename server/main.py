from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from grader.grading_context import GradingContext
from grader.grader import Grader




class Submission(BaseModel):
    task: str
    assignment: str
    criteria: str

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    from parsers.table_reader import TableReader
    TableReader("files/file1.pdf")   
    return {"Hello": "Hi"}

@app.post("/api/submit")
def submit(submission: Submission) -> Any:
    
    config = {'grade_level': 12}




    #grading_context = GradingContext(submission.task, submission.criteria, submission.assignment, config)
    #grader = Grader()
    
    
    
    
    return f"Received {submission}"

    
    
    return 

