import logging
import json
from datetime import datetime

# Configure logging to support both console and file-based JSON logging
log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_format)

# Create custom log handler to log to JSON file
class JsonLogHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        log_entry = json.dumps({"timestamp": str(datetime.now()), "log": log_entry})
        with open('cybercare.json', 'a') as f:
            f.write(log_entry + "\n")

json_handler = JsonLogHandler()
json_handler.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
json_handler.setFormatter(formatter)
logging.getLogger().addHandler(json_handler)

def log(message, level='info'):
    if level == 'info':
        logging.info(message)
    elif level == 'error':
        logging.error(message)
    elif level == 'warning':
        logging.warning(message)
