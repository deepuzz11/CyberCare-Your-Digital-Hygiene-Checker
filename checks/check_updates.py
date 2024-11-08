import subprocess
import platform
from utils.logger import log

def check_updates_linux():
    try:
        result = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True)
        return "upgradable" in result.stdout.lower()
    except Exception as e:
        log(f"Error checking updates on Linux: {e}", "error")
        return None

def check_updates_windows():
    try:
        result = subprocess.run(["winget", "upgrade"], capture_output=True, text=True)
        return "No updates available" not in result.stdout
    except Exception as e:
        log(f"Error checking updates on Windows: {e}", "error")
        return None

def run_check():
    log("Running advanced software updates check...")
    os_platform = platform.system().lower()
    if os_platform == "linux":
        updates_needed = check_updates_linux()
    elif os_platform == "windows":
        updates_needed = check_updates_windows()
    else:
        log("Unsupported OS for updates check", "error")
        return

    if updates_needed is None:
        print("Update check failed.")
        log("Update check failed.", "error")
    elif updates_needed:
        print("System has pending updates.")
        log("System has pending updates.")
    else:
        print("System is up-to-date.")
        log("System is up-to-date.")
