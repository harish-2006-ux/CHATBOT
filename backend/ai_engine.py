import os
import google.generativeai as genai

"""
AI Engine for Shadow Interpreter
Uses Google Gemini 1.0 Pro (stable, supported by v1beta)
"""

# Configure Gemini using API key from environment variables
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# IMPORTANT: Use a model supported by v1beta
model = genai.GenerativeModel("gemini-1.0-pro")


def interpret_query(message: str) -> str:
    try:
        response = model.generate_content(message)

        if response and hasattr(response, "text") and response.text:
            return response.text.strip()

        return "No response generated. Please rephrase your query."

    except Exception as e:
        return f"AI Error: {str(e)}"
