
from fastapi import FastAPI
from pydantic import BaseModel

from agents.Planner import Planner
from agents.executor import Executor
from agents.validator import Validator

app = FastAPI() 

class QueryRequest(BaseModel):
    query: str
    
@app.get("/")
def formula1():
    return {"message": "Welcome to F1"}

@app.post("/process_query")
def process_query(request: QueryRequest):
    planner = Planner()
    executor = Executor()
    validator = Validator()
    
    data = planner.planner(request.query)
    
    summary = executor.executor(request.query, data)
    
    validation_result = validator.validator(request.query, summary)
    
    return {
        "list of APIs that should be used": data,
        "summary": summary,
        "validation_result": validation_result
    }


def main():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":    main()
