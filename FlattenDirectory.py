import os
import shutil

def flatten_directory(source_dir, target_dir, filter_string = '', append_subfolder=False, copy=True):
    """
    Move all files from source_dir and its subdirectories to target_dir.
    If append_subfolder is True, the subfolder name is appended in front of the file name.
    If filter_string is not empty, only files in the subdirectory containing the filter string are moved.
    If copy is True, the files are copied instead of moved.
    """
    # Check if the target directory exists, create if not
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, dirs, files in os.walk(source_dir):

        # Skip files in the subdirectory if filter string is not empty and not in the current directory name
        if filter_string != '' and filter_string not in os.path.basename(root):
            continue

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
                # Move / copy file to target directory
                if copy:
                    shutil.copy(file_path, target_file_path)
                else:
                    shutil.move(file_path, target_file_path)
            else:
                print(f"Duplicate file skipped: {file_path}")

# Usage
source_directory = '/home/jo/RCI/'
target_directory = '/home/jo/RCI/Exams/'
filter_string = 'Altklausuren'
APPEND_SUBFOLDER = True
COPY = True


flatten_directory(source_directory, target_directory, append_subfolder=APPEND_SUBFOLDER, filter_string=filter_string, copy=COPY)
