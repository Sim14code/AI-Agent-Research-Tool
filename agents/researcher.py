from tools.tavily_tool import search_web

def research_agent_step(state):
    query = state["query"]
    result = search_web(query)
    summary = "\n".join([r["content"] for r in result[:3]])  # use top 3 results
    return {
        "summary": summary,
        **state
    }
