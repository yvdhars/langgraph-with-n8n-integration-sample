from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama

# Load Ollama model
llm = ChatOllama(
    model="qwen3.5",
    temperature=0
)

# Agent State
class AgentState(TypedDict):
    input: str
    output: str

# Node Function
def chatbot(state):

    response = llm.invoke(state["input"])

    return {
        "output": response.content
    }

# Build Graph
graph = StateGraph(AgentState)

graph.add_node("chatbot", chatbot)

graph.set_entry_point("chatbot")

graph.add_edge("chatbot", END)

# Compile Agent
agent = graph.compile()