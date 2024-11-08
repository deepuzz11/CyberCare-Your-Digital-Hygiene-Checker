from incident_response.block_ip import block_ip
from incident_response.send_email import send_email
from incident_response.quarantine_file import quarantine_file
from utils.logger import log

def trigger_incident_response(threat_type, threat_data):
    """Trigger appropriate incident response based on the threat type."""
    if threat_type == "compromised_password":
        # Block the IP address and send email about the compromised password
        block_ip(threat_data["ip"])
        send_email(
            subject="Critical Security Alert: Compromised Password",
            body=f"A password breach was detected. IP Address: {threat_data['ip']}. Password: {threat_data['password']}"
        )
    
    elif threat_type == "malicious_file":
        # Quarantine the malicious file and send an email alert
        quarantine_file(threat_data["file_path"])
        send_email(
            subject="Critical Security Alert: Malicious File Detected",
            body=f"A malicious file has been detected and quarantined. File Path: {threat_data['file_path']}"
        )
    
    else:
        log(f"Unknown threat type: {threat_type}", "error")
