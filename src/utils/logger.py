import os
import json
from datetime import datetime

LOGS_FOLDER = "logs"


def ensure_logs_folder():
    if not os.path.exists(LOGS_FOLDER):
        os.makedirs(LOGS_FOLDER)

def log_message(user_msg: str, ai_msg: str):
    ensure_logs_folder()

    filename = os.path.join(
        LOGS_FOLDER,
        f"{datetime.now().strftime('%Y-%m-%d')}.log"
    )

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "user": user_msg,
        "ai": ai_msg
    }
    
    with open(filename, "a") as f:
        f.write(json.dumps(log_entry) + "\n")