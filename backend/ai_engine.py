import os
import google.generativeai as genai

"""
AI Engine for Shadow Interpreter
Uses Google PaLM Text-Bison model (stable, supported by v1beta)
"""

# Configure API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def interpret_query(message: str) -> str:
    try:
        response = genai.generate_text(
            model="models/text-bison-001",
            prompt=message,
            temperature=0.7,
            max_output_tokens=512
        )

        if response and "result" in response and response["result"]:
            return response["result"].strip()

        return "No response generated. Please rephrase your query."

    except Exception as e:
        return f"AI Error: {str(e)}"
