import os
import filecmp
import shutil

def compare_and_copy_files(source_folder1, source_folder2, folder_to_copy_to):
    # Get the list of files in both source folders
    files1 = get_files_list(source_folder1)
    files2 = get_files_list(source_folder2)

    # Compare files in both folders and copy identical files to the destination folder
    for file1 in files1:
        for file2 in files2:
            if are_files_identical(file1, file2):
                copy_file(file1, folder_to_copy_to)
                break
        else:
            print(f"Conflict: File '{os.path.basename(file1)}' has different content")

def get_files_list(folder):
    files_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                files_list.append(file_path)
    return files_list

def are_files_identical(file1, file2):
    return filecmp.cmp(file1, file2, shallow=False)

def copy_file(file_path, destination_folder):
    filename = os.path.basename(file_path)
    destination_path = os.path.join(destination_folder, filename)
    shutil.copy2(file_path, destination_path)
    print(f"File '{filename}' copied to '{destination_folder}'")

# Example usage
source_folder1 = '/Users/micha/Documents/Entwicklung/values-bros-finance/src/backend/app/models'
source_folder2 = '/Users/micha/Documents/Entwicklung/values-bros-finance/src/compute/src/models'
folder_to_copy_to = '/Users/micha/Documents/Entwicklung/GitHub/vbf-shared-models/src/vbfsharedmodels/models'

compare_and_copy_files(source_folder1, source_folder2, folder_to_copy_to)
