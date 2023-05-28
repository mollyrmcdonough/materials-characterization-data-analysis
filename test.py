import os

def search_files(directory, keywords):
    characterization_files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
            for keyword in keywords:
                if keyword.lower() in dirname.lower():
                    subdir_path = os.path.join(dirpath, dirname)
                    subdir_files = os.listdir(subdir_path)
                    for file in subdir_files:
                        # We append a tuple containing both the directory and the file name
                        characterization_files.append((subdir_path, file))
    return characterization_files

# List of keywords to search for in directory names
keywords = ["XRD", "AFM", "TRP", "ARP"]

# Your target directory
directory = '/Users/mollymcdonough/Code/materials-characterization-data-analysis/MBE1-230522A-YO_(Bi,Sb)2Te3 on Al2O3'

characterization_files = search_files(directory, keywords)

# Print only filenames
for _, filename in characterization_files:
    print(filename)
