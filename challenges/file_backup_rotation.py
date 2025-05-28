# Problem 2: Simple File Backup & Rotation
# Problem Statement:
# Write a Python script that takes a target file path as an argument (e.g., ./my_important_data.txt).


# It should create a backup of this file into a subdirectory named backups (relative to the script's location). If the backups directory doesn't exist, the script should create it.
# The backup filename should include a timestamp (e.g., my_important_data_YYYYMMDD_HHMMSS.txt).
# The script should then ensure that only the 3 most recent backup files for this specific target file are kept in the backups directory. Older backups for that target file should be deleted.
import os
import sys
import shutil
import datetime
import glob

def file_backup(log_file):
  try:
    if not os.path.isfile(log_file):
      raise FileNotFoundError(f"The file {log_file} does not exist.")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    backup_dir = os.path.join(script_dir, "../backups")
    print(backup_dir)
    if not os.path.exists(backup_dir):
      os.makedirs(backup_dir)
      
    file_name = os.path.basename(log_file)
    file_base, file_ext = os.path.splitext(file_name)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{file_base}_{timestamp}{file_ext}"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    shutil.copy2(log_file, backup_path)
    print(f"Created backup: {backup_filename}")
    
    backup_pattern = os.path.join(backup_dir, f"{file_base}_*{file_ext}")
    all_backups = glob.glob(backup_pattern)
    
    if len(all_backups) > 3:
        all_backups.sort(key=os.path.getmtime)
        
        for old_backup in all_backups[:-3]:
            os.remove(old_backup)
            print(f"Removed old backup: {os.path.basename(old_backup)}")
    
    return True
      
  except FileNotFoundError as e:
      print(f"Error: {e}")
      return False
  except Exception as e:
      print(f"An unexpected error occurred: {e}")
      return False




if __name__ == "__main__":
        file_path = sys.argv[1]
        file_backup(file_path)