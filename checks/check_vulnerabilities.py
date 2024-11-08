import requests
from utils.logger import log

def check_vulnerabilities(software):
    """Check if the given software has known CVEs."""
    url = f"https://cve.circl.lu/api/cve/{software}"
    response = requests.get(url)
    return response.json()

def run_check():
    log("Running vulnerability scan...")
    print("Enter a software name (e.g., 'apache', 'openssl') to check for known vulnerabilities:")
    software = input("Software: ")
    vulnerabilities = check_vulnerabilities(software)
    
    if vulnerabilities:
        print(f"Found vulnerabilities for {software}:")
        for vuln in vulnerabilities:
            print(f"  - {vuln['id']}: {vuln['summary']}")
            log(f"Vulnerability found for {software}: {vuln['id']} - {vuln['summary']}")
    else:
        print(f"No known vulnerabilities found for {software}.")
        log(f"No vulnerabilities found for {software}.")
