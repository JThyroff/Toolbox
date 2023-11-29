import os
import shutil

def flatten_directory(source_dir, target_dir, append_subfolder=False):
    """
    Move all files from source_dir and its subdirectories to target_dir.
    If append_subfolder is True, the subfolder name is appended in front of the file name.
    """
    # Check if the target directory exists, create if not
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:

            # Construct full file path
            file_path = os.path.join(root, file)

            # Construct target file path
            target_file_path = os.path.join(target_dir, file)


            if (append_subfolder):
                subfolder_name = os.path.basename(root)
                # New file name with subfolder appended
                new_file_name = f"{subfolder_name}_{file}" if root != source_dir else file
                # Construct target file path
                target_file_path = os.path.join(target_dir, new_file_name)

            # Check for duplicate files in the target directory
            if not os.path.exists(target_file_path):
                # Move file to target directory
                shutil.move(file_path, target_file_path)
            else:
                print(f"Duplicate file skipped: {file_path}")

# Usage
source_directory = 'path/to/source/directory'
target_directory = 'path/to/target/directory'
APPEND_SUBFOLDER = True

flatten_directory(source_directory, target_directory, append_subfolder=APPEND_SUBFOLDER)
