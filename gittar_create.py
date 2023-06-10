import os
import subprocess
from dotenv import load_dotenv
import pathlib

load_dotenv()

# Load variables from .env
SOURCE_DIR = os.getenv("SOURCE_DIR")  # Source directory for tar creation
BACKUP_DIR = os.getenv("BACKUP_DIR")  # Destination directory for the tar file

# Convert path to absolute path
SOURCE_DIR = os.path.abspath(SOURCE_DIR)
BACKUP_DIR = os.path.abspath(BACKUP_DIR)

def create():
    # Check if source directory exists
    if not os.path.isdir(SOURCE_DIR):
        raise ValueError(f'SOURCE_DIR does not exist: {SOURCE_DIR}')
    
    # Check if backup directory exists
    if not os.path.isdir(BACKUP_DIR):
        raise ValueError(f'BACKUP_DIR does not exist: {BACKUP_DIR}')

    # Change working directory to source directory
    os.chdir(SOURCE_DIR)

    # Construct the backup file name
    base_name = os.path.basename(os.path.normpath(SOURCE_DIR))  # Gets the base directory name
    tar_name = f"{base_name}.tar.gz"  # Name of tar file
    tar_file = os.path.join(BACKUP_DIR, tar_name)

    print(f"Running command: tar -cvpzf {tar_file} .")
    try:
        subprocess.run(['tar', '-cvpzf', tar_file, '.'], check=True)
        print(f"Backup of {SOURCE_DIR} completed! Backup file: {tar_file}")
    except subprocess.CalledProcessError as e:
        print(f"Backup of {SOURCE_DIR} failed! Error: {e}")
        print(f"Command stdout: {e.stdout}")
        print(f"Command stderr: {e.stderr}")

if __name__ == "__main__":
    create()
