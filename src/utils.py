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
        


