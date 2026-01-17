import os
import shutil
from datetime import datetime

SOURCE_DIR = "datasets"
BACKUP_DIR = "backups"

def backup_data():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"backup_{timestamp}")

    shutil.copytree(SOURCE_DIR, backup_path)
    print(f"Backup created at: {backup_path}")

if __name__ == "__main__":
    backup_data()
