from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):

    result = agent.invoke({
        "input": req.message
    })

    return {
        "response": result["output"]
    }