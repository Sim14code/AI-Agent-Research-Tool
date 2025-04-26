# AI-Agent-Research-Tool



The **AI-Agent-Research-Tool** is a Python-based framework designed to simplify the process of retrieving, summarizing, and drafting responses based on real-time web search results. It integrates AI-driven agents to assist in research, content generation, and decision-making workflows.  

## **Features**
- **Web Search Integration**: Perform live searches on the web and retrieve structured results.
- **Research Summarization**: Summarize key points from search results to facilitate quick understanding.
- **AI-Driven Drafting**: Generate well-articulated responses using AI models like `google.generativeai`.
- **Error Handling**: Robust error handling to ensure smooth operation even in edge cases.

---


## **Getting Started**
These instructions will guide you on how to set up and use the tool on your local machine.

### **Prerequisites**
- Python 3.8 or above
- A valid Google Generative AI API key
- `pip` for package management

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/Sim14code/AI-Agent-Research-Tool.git
   cd AI-Agent-Research-Tool
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment:
   - Create a `.env` file in the root directory.
   - Add your Google Generative AI API key and Tavily Tool API key :
     ```
     GOOGLE_API_KEY=your_api_key_here
     TAVILY_API_KEY=your_api_key_here
     ```

---

## **Usage**
### **1. Importing the Tool**
```python
from tools.tavily_tool import search_web
from main import research_agent_step, drafting_agent_step
```

### **2. Running the Research Agent**
The `research_agent_step` performs a web search and summarizes the results:
```python
state = {"query": "AI advancements in 2025"}
state = research_agent_step(state)
print(state["summary"])  # Outputs summarized research content
```

### **3. Running the Drafting Agent**
The `drafting_agent_step` generates a response based on the research summary and query:
```python
state = drafting_agent_step(state)
print(state["response"])  # Outputs the AI-generated response
```

### **4. Example Workflow**
```python
from tools.tavily_tool import search_web
from main import research_agent_step, drafting_agent_step

state = {"query": "Impact of AI in healthcare"}
state = research_agent_step(state)
state = drafting_agent_step(state)

print("Summary:", state["summary"])
print("Response:", state["response"])
```

---

## **Agents**
### **Research Agent**
The Research Agent handles web searches and generates a summarized output:
- **Input**: A query string (e.g., `"AI advancements in 2025"`).
- **Output**: A summarized version of the top search results.

### **Drafting Agent**
The Drafting Agent uses the research summary to draft a comprehensive response:
- **Input**: A query string and the summarized research content.
- **Output**: A detailed AI-generated answer.

---

