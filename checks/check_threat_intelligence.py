import requests
from utils.logger import log
from incident_response.incident_trigger import trigger_incident_response

def check_password_breach(password, ip_address):
    """Check password against HaveIBeenPwned API."""
    url = f"https://api.pwnedpasswords.com/range/{password[:5]}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            hashes = response.text.splitlines()
            for hash in hashes:
                if hash[0] == password[5:].upper():
                    log(f"Password {password} has been compromised.", "warning")
                    trigger_incident_response("compromised_password", {"ip": ip_address, "password": password})
                    return True
        else:
            log(f"Error checking password: {response.status_code}", "error")
    except requests.RequestException as e:
        log(f"Request error when checking password: {e}", "error")
    return False

def check_file_virus(file_path):
    """Check file using VirusTotal API."""
    api_key = "XXXXXXXXXXXXXX"  # Replace with your actual VirusTotal API key
    url = "https://www.virustotal.com/api/v3/files/"
    headers = {"x-apikey": api_key}

    try:
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(url, headers=headers, files=files)
        
        if response.status_code == 200:
            result = response.json()
            if result.get('data') and result['data']['attributes']['last_analysis_stats']['malicious'] > 0:
                log(f"File {file_path} is flagged as malicious.", "warning")
                trigger_incident_response("malicious_file", {"file_path": file_path})
                return True
            else:
                log(f"File {file_path} is clean.", "info")
        else:
            log(f"Error scanning file: {response.status_code}", "error")
    except requests.RequestException as e:
        log(f"Request error when scanning file: {e}", "error")
    except FileNotFoundError:
        log(f"File not found: {file_path}", "error")
    
    return False

def run_check():
    """Run the threat intelligence checks for password and file."""
    log("Running threat intelligence checks...")

    # Check password breach
    print("Enter a password to check against breaches:")
    password = input("Password: ")
    ip_address = "192.168.1.100"  # Example IP address, replace with actual IP detection method

    if check_password_breach(password, ip_address):
        print("This password has been compromised in a data breach!")
    else:
        print("This password is safe.")

    # Check file for viruses
    print("Enter a file path to scan for viruses:")
    file_path = input("File Path: ")
    
    if check_file_virus(file_path):
        print("This file is flagged as malicious!")
    else:
        print("File is clean.")

