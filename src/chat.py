import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

load_dotenv()

def get_ai_response_stream(conversation_history:list) -> str:
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=conversation_history,
            temperature=0.7,
            stream = True
        )        
        full_response = ""
        for chunk in response:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                full_response+=content
        print()
        return full_response                                               
    except Exception as e:
        print(f"Error:{str(e)}")
    
def mock_chat_response(user_input: str, history: list) -> str:
    """
    Mock AI response with conversation memory.
    """
    response = f"I remember {len(history)} messages. You said: '{user_input}'"
    return response