import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

load_dotenv()

def get_ai_response(conversation_history: list) -> str:
    """
    Get response from OpenAI using conversation history
    """

    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        if not os.getenv("OPENAI_API_KEY"):
            return "ERROR: API key not found. Check your .env file."

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
    
def mock_chat_response(user_input: str, history: list) -> str:
    """
    Mock AI response with conversation memory.
    """
    response = f"I remember {len(history)} messages. You said: '{user_input}'"
    return response