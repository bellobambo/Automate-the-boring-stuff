from pathlib import Path

# Specify the path and name of the new file
file_path = Path('/path/to/new_file.txt')

# Create the new file
file_path.touch()

# Check if the file was created
if file_path.is_file():
    print(f"File '{file_path}' created successfully.")
else:
    print(f"Failed to create file '{file_path}'.")