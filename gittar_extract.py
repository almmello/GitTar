import os
import sys
import subprocess
from dotenv import load_dotenv
from pathlib import Path
import shutil

# Load environment variables
load_dotenv()

# Get environment variables
SOURCE_DIR = os.getenv("SOURCE_DIR")
BACKUP_DIR = os.getenv("BACKUP_DIR")
EXTRACT_DIR = os.getenv("EXTRACT_DIR")

def extract():
    # Get directory name
    dir_name = os.path.basename(os.path.normpath(SOURCE_DIR))  # Gets the base directory name
    # Backup file and snar file path
    BACKUP_FILE = os.path.join(BACKUP_DIR, f"{dir_name}.tar.gz")

    # Check if backup file exists
    if not os.path.isfile(BACKUP_FILE):
        raise ValueError(f'BACKUP_FILE does not exist: {BACKUP_FILE}')
    
    # Check if extract directory exists
    if not os.path.isdir(EXTRACT_DIR):
        raise ValueError(f'EXTRACT_DIR does not exist: {EXTRACT_DIR}')
    
    # Check if extract directory is empty (excluding hidden files)
    if any(os.path.join(EXTRACT_DIR, item) for item in os.listdir(EXTRACT_DIR) if not item.startswith('.')):
        raise ValueError(f'EXTRACT_DIR contains non-hidden files or directories: {EXTRACT_DIR}. Please clean the destination before proceeding.')
    
    # If the directory is empty, delete and recreate it
    shutil.rmtree(EXTRACT_DIR)
    os.makedirs(EXTRACT_DIR)
    
    # Command to extract
    command = ['tar', '-xzf', BACKUP_FILE, '-C', EXTRACT_DIR]

    # Run command
    try:
        print(f"Running command: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True)
        result.check_returncode()
        print(f"Extraction of {BACKUP_FILE} to {EXTRACT_DIR} completed!")
    except subprocess.CalledProcessError as e:
        print(f"Extraction of {BACKUP_FILE} failed! Error: {str(e)}")
        print(f"Command stdout: \n{e.stdout}")
        print(f"Command stderr: \n{e.stderr}")

if __name__ == "__main__":
    extract()
