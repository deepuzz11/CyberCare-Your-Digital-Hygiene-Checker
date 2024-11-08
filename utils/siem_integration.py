from elasticsearch import Elasticsearch
from utils.logger import log

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

def send_to_siem(log_data):
    """Send log data to Elasticsearch (SIEM)."""
    index = "cybercare-logs"
    document = {
        "timestamp": log_data["timestamp"],
        "log": log_data["log"]
    }
    es.index(index=index, body=document)
    log(f"Sent log to SIEM: {log_data['log']}")
