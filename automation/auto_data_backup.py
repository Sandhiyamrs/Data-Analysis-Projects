"""
Simple backup script: copies dataset files to a backup folder with timestamp.
"""
import os
import shutil
from datetime import datetime

SOURCE_DIR = "datasets"
BACKUP_DIR = "backups"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def backup():
    ensure_dir(BACKUP_DIR)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(BACKUP_DIR, f"backup_{timestamp}")
    shutil.copytree(SOURCE_DIR, dest)
    print(f"Backup created at {dest}")

if __name__ == "__main__":
    backup()
