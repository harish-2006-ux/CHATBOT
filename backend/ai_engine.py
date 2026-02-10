import os
import google.generativeai as genai

"""
AI Engine for Shadow Interpreter
Uses Google Gemini 1.5 Flash (supported model)
"""

# Configure Gemini using API key from environment variables
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# IMPORTANT: model name WITHOUT 'models/' prefix
model = genai.GenerativeModel("gemini-1.5-flash")


def interpret_query(message: str) -> str:
    try:
        response = model.generate_content(message)

        if response and hasattr(response, "text") and response.text:
            return response.text.strip()

        return "No response generated. Please rephrase your query."

    except Exception as e:
        return f"AI Error: {str(e)}"
