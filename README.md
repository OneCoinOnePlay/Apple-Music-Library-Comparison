# Apple Music Library Comparison

This Python script is designed for comparing files in an Apple Music library between two specified folders and generating a log file containing information about missing files. It can be useful for verifying the integrity of backups or ensuring that files are correctly synchronized between two directories. The script performs a one-way comparison from the source folder to the destination folder.

## Prerequisites

Before using this script, make sure you have the following:

- Python installed on your system.
- Required Python libraries: `os`, `logging`, and `hashlib`.

## Usage

1. Clone this repository or download the script to your local machine.

2. Edit the script to specify the source and destination folder paths you want to compare. 
   ```python
   source_folder_path = "/Volumes/2TB/MusicBackup"
   destination_folder_path = "/Volumes/2TB/Music/Music/"
   ```
3.Run the script using Python:
   ```python
   python apple_music_library_comparison.py
   ```
3. The script will compare files in the specified folders, compute their hashes, and generate a log file named comparison_log.txt.

4. The log file will contain the following information:

- Source Folder Path
- Destination Folder Path
- Number of Files Checked
- Missing files and their full paths
- The log file will also include the total number of missing files.

Example log file entry:
example_file.mp3 - Hash: 3a4f53c7a2d0e3e7e23c49b13650b617567c1bbd - Full Path: /Volumes/2TB/MusicBackup/example_file.mp3

## Error Handling
In case of any errors during the comparison process, the script will log the error details.

## License
This script is provided under the MIT License.


