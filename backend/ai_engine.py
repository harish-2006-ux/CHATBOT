import os
import cohere

"""
Pure AI Engine using Cohere
No fallback, no rules, no local logic
"""

# Initialize Cohere client
co = cohere.Client(os.getenv("COHERE_API_KEY"))


def interpret_query(message: str) -> str:
    """
    Sends user input directly to Cohere AI
    and returns the AI-generated response.
    """
    try:
        response = co.generate(
            model="command",
            prompt=message,
            max_tokens=300,
            temperature=0.7
        )
        return response.generations[0].text.strip()

    except Exception as e:
        return f"AI Error: {str(e)}"
