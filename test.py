import os

def list_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories

# Replace the path below with your directory path
path_to_check = "/path/to/your/directory"

print("Directories in '{}':".format(path_to_check))
for directory in list_directories(path_to_check):
    print(directory)
