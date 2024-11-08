from checks.check_cryptography import run_check as check_cryptography
from checks.check_firewall import run_check as check_firewall
from checks.check_password_strength import run_check as check_password_strength
from checks.check_services import run_check as check_services
from checks.check_threat_intelligence import run_check as check_threat_intelligence
from checks.check_updates import run_check as check_updates
from checks.check_vulnerabilities import run_check as check_vulnerabilities

from incident_response.block_ip import block_ip
from incident_response.incident_trigger import trigger_incident_response
from incident_response.quarantine_file import quarantine_file
from incident_response.send_email import send_email

from utils.logger import log

def run_all_checks():
    """Run all security checks and respond to incidents."""
    log("Starting CyberCare: Your Digital Hygiene Checker.", "info")

    # Run various security checks and store incidents
    incidents = []
    ip_to_block = None  # Initialize IP to block, if any

    # Check cryptography configuration
    if check_cryptography():
        incidents.append("Cryptography misconfiguration detected.")
    
    # Check firewall settings
    if check_firewall():
        incidents.append("Firewall misconfiguration detected.")

    # Check password strength
    if check_password_strength():
        incidents.append("Weak password detected.")
    
    # Check for unused or misconfigured services
    if check_services():
        incidents.append("Misconfigured services detected.")
    
    # Check for breaches or malicious files using threat intelligence
    if check_threat_intelligence():
        incidents.append("Breach or malicious file detected.")
        # Example: You can dynamically extract IP or file details from incident data
        ip_to_block = "192.168.1.100"  # Example: the IP detected in a breach (this could be dynamic)
    
    # Check for missing software updates
    if check_updates():
        incidents.append("Outdated software detected.")

    # Check for known vulnerabilities
    if check_vulnerabilities():
        incidents.append("Vulnerabilities detected in the system.")

    # Handle any triggered incidents
    if incidents:
        for incident in incidents:
            trigger_incident_response(incident, {"detail": f"Incident details: {incident}"})
            
            # Send email notification about the incident
            send_email("deepikaprabhakaran11@gmail.com", "CyberCare Incident Alert", incident)

        # Perform any necessary automated response actions (e.g., blocking IP or quarantining files)
        if ip_to_block:
            log(f"Blocking IP {ip_to_block} as part of incident response.", "warning")
            block_ip(ip_to_block)  # Dynamically block the detected IP

        suspicious_file = "path/to/suspicious_file.exe"  # Example: Suspicious file path from an incident
        quarantine_file(suspicious_file)  # Quarantine malicious file if applicable

    else:
        log("No incidents detected.", "info")

    log("CyberCare checks complete.", "info")

if __name__ == "__main__":
    run_all_checks()
