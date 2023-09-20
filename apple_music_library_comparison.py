import os
import logging
import hashlib

# Define the source and destination folder paths
source_folder_path = "/Volumes/2TB/Music Music Media Possible Duplicates/Music/"
destination_folder_path = "/Volumes/2TB/Music/Music/"

# Set up logging
log_file = "comparison_log.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

# Function to compute the hash of a file
def calculate_file_hash(file_path):
    sha1_hash = hashlib.sha1()
    with open(file_path, "rb") as file:
        while True:
            data = file.read(65536)  # Read in 64k chunks
            if not data:
                break
            sha1_hash.update(data)
    return sha1_hash.hexdigest()

try:
    # List files in the source folder and compute their hashes
    source_files = {}
    for root, _, files in os.walk(source_folder_path):
        for file in files:
            if file != ".DS_Store":  # Ignore .DS_Store files
                file_path = os.path.join(root, file)
                hash_value = calculate_file_hash(file_path)
                source_files[file] = (hash_value, file_path)
    
    # List files in the destination folder and compute their hashes
    destination_files = {}
    for root, _, files in os.walk(destination_folder_path):
        for file in files:
            if file != ".DS_Store":  # Ignore .DS_Store files
                file_path = os.path.join(root, file)
                hash_value = calculate_file_hash(file_path)
                destination_files[file] = (hash_value, file_path)
    
    # Identify missing files in the source folder compared to the destination folder
    missing_files = [file for file in source_files if file not in destination_files or source_files[file][0] != destination_files[file][0]]
    
    # Save the list of missing files, their full paths, and hashes to a text file
    with open(log_file, "w") as output_file:
        output_file.write(f"Source Folder Path: {source_folder_path}\n")
        output_file.write(f"Destination Folder Path: {destination_folder_path}\n")
        output_file.write(f"Number of Files Checked: {len(source_files)}\n")
        output_file.write("Missing files and their full paths:\n")
        missing_count = 0
        for i, file in enumerate(missing_files):
            file_path = source_files[file][1]
            hash_value = source_files[file][0]
            output_file.write(f"{i + 1}. {file} - Hash: {hash_value} - Full Path: {file_path}\n")
            missing_count += 1
        
        output_file.write(f"Total Missing Files: {missing_count}\n")

    logging.info(f"Missing files have been saved to {log_file}. Total missing files: {missing_count}")
except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
