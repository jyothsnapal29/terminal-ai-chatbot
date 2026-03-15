from chat import mock_chat_response
from utils import log_message, ensure_logs_folder
from prompts import SYSTEM_PROMPT

def main():
    ensure_logs_folder()
    print("Welcome to AI Chatbot")
    print(f"Type 'Exit' or 'Quit' to end the conversation")

    conversation_memory = [
        {"role":"system", "content": SYSTEM_PROMPT}
    ]

    while(True):
        user_input = input("You:")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

        conversation_memory.append({"role":"user", "content":user_input})
        ai_response = mock_chat_response(user_input, conversation_memory)
        conversation_memory.append({"role":"assistant", "content":ai_response})
        log_message(user_input, ai_response)
        print(f"Chatbot:{ai_response}")

if __name__ == '__main__':
    main()