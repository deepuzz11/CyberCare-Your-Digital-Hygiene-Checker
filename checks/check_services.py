import psutil
from utils.logger import log

def list_system_services():
    inactive_services = []
    all_services = psutil.win_service_iter() if psutil.WINDOWS else psutil.process_iter()
    
    for service in all_services:
        if service.status() == psutil.STATUS_ZOMBIE:  # Check if the service is inactive or a zombie process
            inactive_services.append(service.name())
    return inactive_services

def run_check():
    log("Running advanced services check...")
    inactive_services = list_system_services()
    if inactive_services:
        print(f"Found inactive or zombie services: {', '.join(inactive_services)}")
        log(f"Inactive or zombie services detected: {', '.join(inactive_services)}")
    else:
        print("No inactive services detected.")
        log("No inactive services detected.")
