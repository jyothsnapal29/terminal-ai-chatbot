import os
from dotenv import load_dotenv
from openai import OpenAI
from utils.logger import log_message

#Load environment variables
load_dotenv()

#Initalize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
client  = OpenAI(api_key=api_key) if api_key else None

def get_ai_response_stream(conversation_history:list) -> str:
    """
        Get AI response using streaming from OpenAI API.
        Prints chunks as they arrive and returns full response.
        Fallbacks to mock response if API key is missing or error occurs.
    """
    last_user_msg = conversation_history[-1]["content"]

    try:
        if client is None:
            return f"[Mock] You said: '{last_user_msg}' | Total messages: {len(conversation_history)}"

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history,
            temperature=0.7,
            stream=True
        )

        full_response = ""
        for chunk in response:
            content = chunk.choices[0].delta.get("content")
            if content:
                print(content, end="", flush=True)
                full_response += content
        print()

        if not full_response:
            return f"[Mock] Empty response fallback for: '{last_user_msg}'" 
        return full_response

    except Exception as e:
        log_message(f"API Error on message: {last_user_msg}", str(e))
        return f"[Mock] You said: '{last_user_msg}' | Total messages: {len(conversation_history)}"