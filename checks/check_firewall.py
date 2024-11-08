import subprocess
import platform
from utils.logger import log

def firewall_status_linux():
    try:
        result = subprocess.run(["ufw", "status"], capture_output=True, text=True)
        return "active" in result.stdout.lower()
    except Exception as e:
        log(f"Error checking firewall on Linux: {e}", "error")
        return None

def firewall_status_windows():
    try:
        result = subprocess.run(["netsh", "advfirewall", "show", "allprofiles"], capture_output=True, text=True)
        return "State ON" in result.stdout
    except Exception as e:
        log(f"Error checking firewall on Windows: {e}", "error")
        return None

def run_check():
    log("Running advanced firewall status check...")
    os_platform = platform.system().lower()
    if os_platform == "linux":
        status = firewall_status_linux()
    elif os_platform == "windows":
        status = firewall_status_windows()
    else:
        log("Unsupported OS for firewall check", "error")
        return

    if status is None:
        print("Firewall check failed.")
        log("Firewall check failed.", "error")
    elif status:
        print("Firewall is active.")
        log("Firewall is active.")
    else:
        print("Firewall is inactive. Consider enabling it for protection.")
        log("Firewall is inactive.")
