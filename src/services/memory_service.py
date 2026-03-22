
def trim_conversation_history(history: list, max_messages: int = 10) -> list:
    """
        Keeps only the last 'max_messages' messages, always preserving system prompt.
    """
    if not history:
        return history
    system_prompt = [history[0]] if history[0]["role"] == "system" else []
    non_system = history[1:]
    trimmed = non_system[-max_messages:]
    return system_prompt + trimmed