import os
import shutil
import sys

#We will make sure that the user has listed a folder path
if len(sys.argv) < 2:
    print("Error: Please provide input file")
    sys.exit(1)
#When we pass the inital test to see if user has given us a path we will assign it
target_directory = sys.argv[1]

#We will now make sure that the path actually exists and is not given by error
if not os.path.exists(target_directory):
    print("Error: Target directory does not exist")
    sys.exit(1)
if not os.path.isdir(target_directory):
    print("Error: Target directory is not a directory, it is a file")
    sys.exit(1)
print(f"succesfully located directory: {target_directory}")

#The extension map will let the program know what folder we will be moving each type of file
Extension_Map = {
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.heic': 'Images',
    'doc': 'Document',
    '.docx': 'Document',
    '.txt': 'Document',
    '.pdf': 'Documents',
    '.epub': 'books',
    '.7z' : 'Miscellaneous',
    '.gz' : 'Miscellaneous',
    '.tar': 'Miscellaneous',
    '.dmg': 'Miscellaneous',
    '.romfs' : 'Miscellaneous',
    '.zip': 'Projects',
    '.rts': 'Projects',
    '.py': 'Projects',
    '.jar': 'Projects',
    '.csv' : 'Projects',
    '.xslx': 'Projects',
}

#We are going to look at every file in the directory using a for loop
for item in os.listdir(target_directory):
    #Item will only give us the name of the file not where it is so we need to join it together
    full_path = os.path.join(target_directory, item)
    #We then make sure we are not looking at a folder but an actual file
    if os.path.isfile(full_path):
        #We get our file name and extension and we assign them to different variables using the split text
        file_name, file_extension = os.path.splitext(item)
        file_extension = file_extension.lower()

        #We will use our mapping to analyze and separate the files into their corresponding folder
        target_folder = Extension_Map.get(file_extension,"Others")
        print(f"File: {item} -> {target_folder}")
