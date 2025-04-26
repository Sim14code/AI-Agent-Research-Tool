from graph.langgraph_flow import build_graph

def main():
    query = input("🔍 Enter your research query: ")
    agent = build_graph()
    result = agent.invoke({"query": query})
    print("\n🧠 Final Response:")
    print(result["response"])

if __name__ == "__main__":
    main()
