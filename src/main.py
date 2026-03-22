from core.chat import get_ai_response_stream
from core.prompts import SYSTEM_PROMPT
from services.token_service import count_tokens
from services.memory_service import trim_conversation_history
from utils.logger import log_message,ensure_logs_folder

MAX_HISTORY_MESSAGES = 10    
MAX_TOKENS = 1500

def main():
    ensure_logs_folder()
    print("Welcome to AI Terminal Chatbot (Streaming Enabled)")
    print("Type 'Exit' or 'Quit' to end the conversation")
    print("Type '/clear' to reset conversation\n")

    conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ["exit", "quit"]:
                print("Chatbot: Goodbye!")
                break

            if user_input.lower() == "/clear":
                conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]
                print("Chatbot: Conversation history cleared.\n")
                continue

            conversation_history.append({"role": "user", "content": user_input})
            conversation_history = trim_conversation_history(conversation_history, max_messages=MAX_HISTORY_MESSAGES)

            # Count tokens
            total_tokens = count_tokens(conversation_history)
            if total_tokens > MAX_TOKENS:
                print(f"Warning: Conversation tokens exceeded {MAX_TOKENS} ({total_tokens} tokens)")

            print("Chatbot: ", end="", flush=True)
            ai_response = get_ai_response_stream(conversation_history)
            if ai_response.startswith("[Mock]"):
                print(ai_response)
            conversation_history.append({"role": "assistant", "content": ai_response})

            log_message(user_input, ai_response)
            print()

        except KeyboardInterrupt:
            print("\nChatbot: Goodbye!")
            break
        except Exception as e:
            print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()