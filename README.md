# CyberCare: Your Digital Hygiene Checker

CyberCare is a Python-based security auditing utility designed to monitor and enhance your system's digital hygiene. It performs various checks to identify potential security issues and provides actionable recommendations for improving security. 

## Features

CyberCare includes several security modules:
- **Cryptographic Health Check**: Verifies SSL/TLS certificate configurations of specified domains to ensure secure communication.
- **Firewall Status Check**: Checks if the system's firewall is active to safeguard against unauthorized access.
- **Password Strength Evaluation**: Assesses password complexity and entropy to ensure strong password practices.
- **System Services Audit**: Detects inactive or zombie services that could indicate potential vulnerabilities.
- **Threat Intelligence Checks**: Checks for breached passwords and scans files for viruses using third-party APIs.
- **Software Updates Check**: Scans for outdated software and recommends updates.
- **Vulnerability Assessment**: Scans for known vulnerabilities in specified software using the CVE database.

The program also includes incident response mechanisms like blocking IP addresses and quarantining files if malicious activity is detected.

## Installation

### Prerequisites
- Python 3.8 or later
- Recommended to run on Windows or Linux with administrative privileges.
- Install dependencies listed in `requirements.txt` (run `pip install -r requirements.txt`).

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/username/CyberCare-Your-Digital-Hygiene-Checker.git
   cd CyberCare-Your-Digital-Hygiene-Checker

2. (Optional) Set up a virtual environment:
    ``` bash
    python -m venv env
    source env/bin/activate  # Linux/macOS
    env\Scripts\activate     # Windows

3. Configure API keys (e.g., VirusTotal API key) in the check_threat_intelligence.py file.

## Usage

To run all checks and initiate any necessary incident response actions, use the following command:

    ```bash
    python cybercare_main.py
    ``` 
    
## Example Usage
When running the script, CyberCare will:
- Check cryptographic settings for secure HTTPS connections.
- Check firewall status and provide recommendations.
- Assess password strength with entropy calculations.
- Identify inactive or zombie services.
- Use threat intelligence to detect breached passwords and flag malicious files.
- Check for software updates.
- Scan for known software vulnerabilities.

## Response Actions
In case of a detected issue, CyberCare may automatically:
- Block a suspicious IP address.
- Quarantine a malicious file.
- Send email alerts to specified administrators.

## File Structure
- **cybercare_main.py**: Main script that orchestrates all checks and responses.
- **checks/**: Contains modules for each security check.
  - `check_cryptography.py`: Checks SSL/TLS certificate settings.
  - `check_firewall.py`: Verifies firewall status.
  - `check_password_strength.py`: Evaluates password entropy.
  - `check_services.py`: Lists and flags inactive services.
  - `check_threat_intelligence.py`: Detects password breaches and scans files.
  - `check_updates.py`: Verifies if updates are available.
  - `check_vulnerabilities.py`: Checks software for known vulnerabilities.
- **incident_response/**: Contains modules for handling incidents.
  - `block_ip.py`: Blocks suspicious IPs.
  - `incident_trigger.py`: Initiates incident responses.
  - `quarantine_file.py`: Quarantines flagged files.
  - `send_email.py`: Sends incident alerts.
- **utils/logger.py**: Logs messages to the console and a log file for tracking events.

## Configuration
- **Setting API Keys**: Place API key (e.g., VirusTotal) in `check_threat_intelligence.py`.
- **Customize Incident Responses**: Modify the actions in `cybercare_main.py` to add specific incident response rules.

## Dependencies
To install necessary Python libraries, use:
```bash
pip install -r requirements.txt
This includes:

- **psutil**: For monitoring system services.
- **requests**: For HTTP requests to third-party APIs.
- **ssl**: For SSL/TLS certificate checks.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

CyberCare is a proactive way to keep your system secure and efficient. Regularly running this tool will help you stay ahead of potential threats and enhance your digital hygiene.
