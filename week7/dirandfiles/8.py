import os

file_path = "path/to/file.txt"
if os.path.exists(file_path) and os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
    os.remove(file_path)
    print(f"File {file_path} deleted")
else:
    print("no file")
