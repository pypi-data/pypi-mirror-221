import os
import argparse
import platform
import subprocess
from collections import defaultdict
from modules.duplicate_zip_files import check_single_zip_for_duplicates


def get_file_hash(file_path):
    """Calculate the MD5 hash of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The MD5 hash of the file.

    """
    try:
        if platform.system() == "Darwin":
            # macOS (use md5 command)
            md5_output = subprocess.check_output(["md5", file_path], universal_newlines=True)
            file_hash = md5_output.split()[-1]  # Extract the hash from the output
            return file_hash
        else:
            # Linux/Unix-based systems (use md5sum command)
            md5sum_output = subprocess.check_output(["md5sum", file_path], universal_newlines=True)
            file_hash = md5sum_output.split()[0]  # Extract the hash from the output
            return file_hash
    except subprocess.CalledProcessError as e:
        # Handle any errors that might occur during the md5sum command execution
        print(f"Error calculating hash for {file_path}: {e}")
        return None
    

def check_files_in_folder(folder_path, calculate_file_sizes=True):
    """Check for duplicate files in a folder.

    This function traverses through the specified folder and its subdirectories,
    calculates the MD5 hash of each file, and identifies duplicate files by their hashes.

    Args:
        folder_path (str): The path to the folder.

    """
    # Using collections module defaultdict
    # Using a single dictionary to store duplicate files based on hash and size
    duplicate_files = defaultdict(lambda: defaultdict(list))
    
    # Traverse through the folder and its subdirectories
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = get_file_hash(file_path) # Calculate the hash of the file
            # file_hashes[file_hash].append(file_path) # Store the file path with its hash
            
            if calculate_file_sizes:
                file_size = os.path.getsize(file_path)
                file_info = (file_path, file_hash)  # Create a tuple with file_path and file_hash
                duplicate_files[file_size][file_hash].append(file_info)
                
            # Store the file path with its hash in the dictionary
            duplicate_files[file_hash]['file_paths'].append(file_path)
        
        for subfolder in dirs:
            subfolder_path = os.path.join(root, subfolder)
            check_files_in_folder(subfolder_path, calculate_file_sizes)  # Recursive call to check files in nested folder

    # Iterate over the file hashes and their corresponding file paths
    for size, hash_dict in duplicate_files.items():
        for file_hash, file_info_list in hash_dict.items():
            if file_hash == 'file_paths':
                continue
                
            if len(file_info_list) > 1: # Check if there are multiple file paths with the same hash
                print(f"Duplicate files with hash {file_hash} and size {size} bytes:")
                for file_info in file_info_list:
                    file_path, _ = file_info  # Unpack the tuple, but we only need the file_path
                    print(f"Name: {os.path.basename(file_path)}")
                    print(f"Absolute Path: {file_path}")
                print()

    if not calculate_file_sizes:
        for file_hash, file_paths in duplicate_files.items():
            if file_hash == 'file_paths':
                continue

            if len(file_paths) > 1:
                print(f"Duplicate files with hash {file_hash}:")
                for file_path in file_paths:
                    print(file_path)
                print()

    return duplicate_files

def print_duplicate_zip_files(folder_path, calculate_sizes):
    """Print duplicate files in zip archives in the specified folder."""
    # Traverse through the folder and its subdirectories
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            if file_name.endswith('.zip'):
                duplicate_file_paths = check_single_zip_for_duplicates(file_path)
                if duplicate_file_paths:
                    print(f"Duplicate files in {file_name}:")
                    for duplicate_file_path in duplicate_file_paths:
                        print(duplicate_file_path)
                    print()
                else:
                    print(f"No duplicates in {file_name}")
                    print()

        for subfolder in dirs:
            subfolder_path = os.path.join(root, subfolder)
            check_files_in_folder(subfolder_path, calculate_sizes)  # Recursive call to check files in nested folder

    
def main():
    parser = argparse.ArgumentParser(description='Check for duplicate files in a folder.')
    parser.add_argument('-f', '--folder', required=True, help='Path to the folder')
    parser.add_argument('-d', '--delete', action='store_true', help='Flag to enable deletion of duplicates')
    parser.add_argument('-o', '--output', help='Output file path to save the duplicates in TSV format')

    args = parser.parse_args()

    folder_path = args.folder
    enable_delete = args.delete
    output_file = args.output
    calculate_sizes = True  # Set calculate_sizes to True by default

    duplicate_files = check_files_in_folder(folder_path)

    # After checking for duplicate files in the folder, print duplicate zip files
    print_duplicate_zip_files(folder_path, calculate_sizes)

    found_duplicates = False
    duplicates_to_print = set()
    for size, hash_dict in duplicate_files.items():
        for file_hash, file_info_list in hash_dict.items():
            if file_hash == 'file_paths':
                continue

            if len(file_info_list) > 1:
                found_duplicates = True
                # Store the duplicates for later printing
                for file_info in file_info_list[1:]:
                    file_path, _ = file_info
                    duplicates_to_print.add(os.path.basename(file_path))

    if not found_duplicates:
        print("\033[32mNo duplicates found.\033[0m")
    elif duplicates_to_print and found_duplicates:
        if enable_delete:
            print("\033[33mType 'delete' to confirm deletion of duplicates or press enter to skip. \033[0m")
            user_input = input(">>")
            if user_input.strip().lower() == 'delete':
                # Delete the duplicate files permanently
                for size, hash_dict in duplicate_files.items():
                    for file_hash, file_info_list in hash_dict.items():
                        if file_hash == 'file_paths':
                            continue

                        if len(file_info_list) > 1:
                            for file_info in file_info_list[1:]:
                                file_path, _ = file_info
                                os.remove(file_path)
                            print(f"\033[31mDeleted duplicate files with hash {file_hash} and size {size} bytes.\033[0m")
                print("\033[32mDeletion of duplicate files completed.\033[0m")
            else:
                print("\033[32mDeletion canceled. Duplicates are still available.\033[0m")
        else:
            print("\033[32mDuplicates are still available.\033[0m")

    if enable_delete and not found_duplicates:
        print("\033[33mNo duplicates found. Nothing to delete.\033[0m")

        # Save duplicates info to the output file in TSV format if provided
    if output_file and duplicates_to_print:
        with open(output_file, 'w') as f:
            f.write("Name\tAbsolute Path\n")
            for file_name in sorted(duplicates_to_print):
                file_path = os.path.join(folder_path, file_name)
                f.write(f"{file_name}\t{file_path}\n")


if __name__ == '__main__':
    main()
