import json
from datetime import datetime

LOG_FILE = "system_logs.json"

def log_event(event):
    event["timestamp"] = datetime.utcnow().isoformat()

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")