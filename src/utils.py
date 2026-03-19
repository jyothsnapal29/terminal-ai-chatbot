import os
from datetime import datetime

LOGS_FOLDER = "logs"
LOG_FILE = os.path.join(LOGS_FOLDER, "chat_log.txt")

def ensure_logs_folder():
    """
        Creates log folder if it does not exist
    """
    if not os.path.exists(LOGS_FOLDER):
        os.mkdir(LOGS_FOLDER)

def log_message(user_input, ai_response):
    """
        Logs the conversation to the file
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] User:{user_input}\n")
        f.write(f"[{timestamp}] AI: {ai_response}\n")

def token_tracking(text: str) -> int:
    """
        Rough token estimation.
        1 token = 4 characters
    """
    return len(text) // 4

def track_cost(input_tokens: int, output_tokens: int)-> float:
    """
        Rough estimation of the cost for gpt-4-mini
    """
    cost_per_1k_tokens = 0.0000015
    total_tokens = input_tokens + output_tokens
    return (total_tokens / 1000) * cost_per_1k_tokens
        


