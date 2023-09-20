# Apple Music Library Comparison Repository

This repository contains two Python scripts for comparing and managing files in an Apple Music library. You can use these scripts to verify the integrity of backups, ensure correct synchronization, and manage missing files between two specified folders.

---

## Script 1: Apple Music Library Comparison Script

### Description

The `apple_music_library_comparison.py` script performs a one-way comparison from the source folder to the destination folder and generates a log file containing information about missing files in the destination folder.

### Prerequisites

Before using this script, make sure you have the following:

- Python installed on your system.
- Required Python libraries: `os`, `logging`, and `hashlib`.

### Usage

1. Clone this repository or download the script to your local machine.

2. Edit the script to specify the source and destination folder paths you want to compare.

   ```python
   source_folder_path = "/Volumes/2TB/MusicBackup"
   destination_folder_path = "/Volumes/2TB/Music/Music/"
   ```

3. Run the script using Python:

   ```python
   python apple_music_library_comparison.py
   ```

#### How It Works

The script will compare files in the specified folders, compute their hashes, and generate a log file named `comparison_log.txt`. It performs a one-way comparison from the source folder to the destination folder.

The log file will contain information about missing files in the destination folder.

In case of any errors during the comparison process, the script will log the error details.

#### Log File Format

The log file will contain the following information:

- Source Folder Path
- Destination Folder Path
- Number of Files Checked
- Missing files and their full paths
- The log file will also include the total number of missing files.

An example log output is included 'comparison_log (example).txt'

---

## Script 2: Apple Music Library File Management Script

### Description

The `apple_music_library_file_management.py` script builds upon the first script by offering additional functionality to manage missing files in an Apple Music library. It identifies missing files and, if their count is below a specified threshold, copies them to a specified folder.

### Prerequisites

This script has the same prerequisites as the first script:

- Python installed on your system.
- Required Python libraries: `os`, `logging`, and `hashlib`.

### Usage

To use the Apple Music Library File Management Script, follow these steps:

1. Clone this repository or download the script to your local machine.

2. Edit the script to specify the following parameters:

   ```python
   source_folder_path = "/Volumes/2TB/MusicBackup/"
   destination_folder_path = "/Volumes/2TB/Music/Music/"
   missing_files_path = "/Volumes/2TB/Missing/"
   max_missing_files_prompt = 100  # Maximum number of missing files before prompting the user
   ```

3. Run the script using Python:

   ```python
   python apple_music_library_file_management.py
   ```

#### How It Works

The script will perform the same one-way comparison as the first script, identifying missing files in the source folder compared to the destination folder.

It will also attempt to copy missing files to the specified folder (`missing_files_path`) if the number of missing files is below a certain threshold (`max_missing_files_prompt`).

The script logs its actions and errors in the same `comparison_log.txt` file used by the first script.

If the number of missing files exceeds the threshold, the script will log a warning and not attempt to copy the files.

### License

Both scripts are provided under the MIT License.
