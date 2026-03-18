from chat import get_ai_response, mock_chat_response
from utils import log_message, ensure_logs_folder
from prompts import SYSTEM_PROMPT

USE_MOCK = True 

def main():
    ensure_logs_folder()
    print("Welcome to AI Chatbot")
    print(f"Commands: /exit, /clear, /history")

    conversation_history = [
        {"role":"system", "content": SYSTEM_PROMPT}
    ]

    while(True):
        user_input = input("You:")
        if user_input.lower() in ["exit", "quit", "/exit"]:
            print("Chatbot: Goodbye!")
            break

        if user_input.lower() == '/clear':
            conversation_history = [{"role":"system", "content": SYSTEM_PROMPT}]
            print("Chatbot memory cleared")
            continue

        if user_input.lower() == '/history':
            print("\n Last 5 messages")
            for message in conversation_history[-5:]:
                print(f"{message['role'].upper()}:{message['content']}")
            print('----------------\n')
            continue

        conversation_history.append({"role":"user", "content":user_input})
        # Switch between mock and real API
        if USE_MOCK:
            ai_response = mock_chat_response(user_input, conversation_history)
        else:
            ai_response = get_ai_response(conversation_history)
        conversation_history.append({"role":"assistant", "content":ai_response})
        log_message(user_input, ai_response)
        print(f"Chatbot:{ai_response}")

if __name__ == '__main__':
    main()