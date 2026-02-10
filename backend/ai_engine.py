import os
import google.generativeai as genai

"""
AI Engine for Shadow Interpreter
Uses Google Gemini 1.5 Flash (current, supported model)
"""

# Configure Gemini with API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a CURRENT model (gemini-pro is deprecated)
model = genai.GenerativeModel("models/gemini-1.5-flash")


def interpret_query(message: str) -> str:
    try:
        response = model.generate_content(message)

        if response and hasattr(response, "text") and response.text:
            return response.text.strip()

        return "No response generated. Please rephrase your query."

    except Exception as e:
        # Temporary debug (remove later if you want)
        return f"AI Error: {str(e)}"
