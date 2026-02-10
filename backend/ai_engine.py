import os
from openai import OpenAI

"""
AI Engine for Shadow Interpreter
Uses OpenAI Chat Completions API
"""

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def interpret_query(message: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are Shadow Interpreter, an intelligent AI assistant."
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            temperature=0.7,
            max_tokens=400
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"AI Error: {str(e)}"
