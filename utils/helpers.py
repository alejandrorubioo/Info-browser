from datetime import datetime
import pytz
import json

# Function to store log entries
def guardar_log(data, request):
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    timestamp = datetime.now(pytz.timezone("Europe/Madrid")).strftime("%d/%m/%Y %H:%M")

    log_entry = {
        'timestamp': timestamp,
        'ip': ip,
        **data
    }

    with open("log_usuarios.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
