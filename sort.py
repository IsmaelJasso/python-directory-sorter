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
