import shutil
import os
import tempfile
from utils.logger import log

def quarantine_file(file_path):
    """Move a suspicious file to a temporary quarantine folder."""
    
    # Create a temporary directory using tempfile
    try:
        quarantine_folder = tempfile.mkdtemp()  # Create a temporary directory
        log(f"Temporary quarantine folder created: {quarantine_folder}", "info")
        
        # Move the suspicious file to the quarantine folder
        filename = os.path.basename(file_path)
        quarantine_path = os.path.join(quarantine_folder, filename)
        
        # Move the file to the temp quarantine folder
        shutil.move(file_path, quarantine_path)
        
        log(f"Quarantined file {file_path} to {quarantine_path}.", "warning")
        print(f"File {file_path} has been quarantined to: {quarantine_path}")
    except Exception as e:
        log(f"Failed to quarantine file {file_path}: {str(e)}", "error")
