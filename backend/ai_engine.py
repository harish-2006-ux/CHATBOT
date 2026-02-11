import os
import cohere

"""
Pure AI Engine using Cohere Chat API
(Generate API is deprecated)
"""

# Initialize Cohere client
co = cohere.Client(os.getenv("COHERE_API_KEY"))


def interpret_query(message: str) -> str:
    try:
        response = co.chat(
            model="command-r",
            message=message,
            temperature=0.7,
            max_tokens=300
        )

        return response.text.strip()

    except Exception as e:
        return f"AI Error: {str(e)}"
