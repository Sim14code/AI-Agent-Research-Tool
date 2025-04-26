import os
from langchain_community.tools.tavily_search.tool import TavilySearchResults

def search_web(query):
    tool = TavilySearchResults(api_key=os.getenv("TAVILY_API_KEY"))
    return tool.run(query)
