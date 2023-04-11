import os
import shutil

path = "folder"
try:
    #os.remove(path)
    #os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print(path + " not found")
except PermissionError:
    print("The file is empty.")
else:
    print(path + " has been deleted")




