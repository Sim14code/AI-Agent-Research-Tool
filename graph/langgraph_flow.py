from langgraph.graph import StateGraph, END
from agents.researcher import research_agent_step
from agents.drafter import drafting_agent_step
from typing import TypedDict

class ResearchState(TypedDict):
    query: str
    summary: str
    response: str

def build_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("research", research_agent_step)
    graph.add_node("draft", drafting_agent_step)

    graph.set_entry_point("research")
    graph.add_edge("research", "draft")
    graph.add_edge("draft", END)

    return graph.compile()
