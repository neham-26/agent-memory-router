from fastapi import FastAPI
from pydantic import BaseModel

from main import process_query

app = FastAPI(
    title="AI Memory Router API",
    description="Routes user queries to the correct memory backend.",
    version="1.0.0"
)


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {
        "message": "Welcome to the AI Memory Router API!"
    }


@app.post("/ask")
def ask_question(request: QueryRequest):

    memory_type, context, answer = process_query(request.query)

    return {
        "memory_type": memory_type,
        "context": context,
        "answer": answer
    } 