def mock_chat_response(user_input: str, history: list) -> str:
    '''
        Mock AI reponse functionwith conversation history
    '''
    response = f"I remember {len(history)} messages. Your message: '{user_input}'"
    return response