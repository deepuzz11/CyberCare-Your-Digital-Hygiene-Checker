import platform
import subprocess
from utils.logger import log
from quarantine_file import quarantine_file
def block_ip_linux(ip_address):
    """Block IP address on Linux using iptables."""
    try:
        subprocess.run(f"sudo iptables -A INPUT -s {ip_address} -j DROP", shell=True, check=True)
        log(f"Blocked IP {ip_address} on Linux.", "warning")
        print(f"IP {ip_address} has been blocked.")
    except subprocess.CalledProcessError as e:
        log(f"Failed to block IP {ip_address}: {str(e)}", "error")

def block_ip_windows(ip_address):
    """Block IP address on Windows using netsh."""
    try:
        subprocess.run(f"netsh advfirewall firewall add rule name=\"Block {ip_address}\" dir=in action=block remoteip={ip_address}", shell=True, check=True)
        log(f"Blocked IP {ip_address} on Windows.", "warning")
        print(f"IP {ip_address} has been blocked.")
    except subprocess.CalledProcessError as e:
        log(f"Failed to block IP {ip_address}: {str(e)}", "error")

def block_ip(ip_address):
    """Block IP address depending on the platform (Linux/Windows)."""
    os_platform = platform.system().lower()
    if os_platform == "linux":
        block_ip_linux(ip_address)
    elif os_platform == "windows":
        block_ip_windows(ip_address)
    else:
        log(f"Unsupported OS for blocking IP: {os_platform}", "error")

def handle_incident(incident_type, incident_details):
    """Handle the incident and block IP dynamically based on the type."""
    if incident_type == "brute_force":
        # Example: dynamically getting the IP from the incident details
        attacking_ip = incident_details.get("attacking_ip")
        if attacking_ip:
            log(f"Brute force detected from IP: {attacking_ip}. Blocking IP...")
            block_ip(attacking_ip)  # Dynamically block the detected IP
        else:
            log("No attacking IP found in the incident details.", "error")
    
    elif incident_type == "malicious_file":
        suspicious_file = incident_details.get("file_path")
        if suspicious_file:
            log(f"Malicious file detected: {suspicious_file}. Quarantining...")
            quarantine_file(suspicious_file)  # Assuming quarantine_file function exists
        else:
            log("No suspicious file path found in the incident details.", "error")
    
    else:
        log(f"Unknown incident type: {incident_type}", "error")
    
#     # Example: You could send a report or further actions here (e.g., sending email alerts)

# # Example of triggering the incident handler
# incident_data = {
#     "incident_type": "brute_force",
#     "attacking_ip": "192.168.1.100"
# }

# handle_incident(incident_data["incident_type"], incident_data)
