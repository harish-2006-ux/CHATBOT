import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def interpret_query(message: str) -> str:
    try:
        response = model.generate_content(message)
        if response and response.text:
            return response.text.strip()
        return "No response generated."
    except Exception:
        return "Shadow link unstable. Retry command."
