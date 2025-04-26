import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")


def drafting_agent_step(state):
    summary = state.get("summary", "")
    query = state.get("query", "")

    prompt = f"""
    You are an AI research assistant. Based on the research summary, answer the query.Keep it very focussed and formatted as a list of bullet points.
    Bold the important points and use markdown formatting. Do not add any extra information or context.
    Query: {query}
    Summary: {summary}

    Answer:
    """

    try:
        response = model.generate_content(prompt)
        return {
            "response": response.text,
            **state
        }
    except Exception as e:
        print("❌ Drafting error:", e)
        return {
            "response": "Error during drafting.",
            **state
        }
