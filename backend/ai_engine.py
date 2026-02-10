import os
import google.generativeai as genai

"""
AI Engine for Shadow Interpreter
Uses Google Gemini via the official GenerativeModel API
"""

# Configure API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a supported model
model = genai.GenerativeModel("gemini-pro")


def interpret_query(message: str) -> str:
    try:
        response = model.generate_content(message)

        if response and response.text:
            return response.text.strip()

        return "No response generated. Please rephrase your question."

    except Exception as e:
        return f"AI Error: {str(e)}"
