import os
import mpy_cross
import subprocess
import shutil
from time import sleep

def convert_py_into_mpy(source, dest):
    print("creating mpy destination folder")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    
    
    print("creating mpy files")
    for root, dirs, files in os.walk(source):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if root == source and file in ["boot.py", "main.py", "config.py"] :
                pass
            elif file != "__init__.py" and file.endswith(".py") :
                file_path = os.path.join(root, file)
                mpy_cross.run(file_path, stdout=subprocess.PIPE)
    
    
    print("moving / copying files into new folder")
    for root, dirs, files in os.walk(source):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            file_path   = os.path.join(root, file)
            folder_dest = dest + root[len(source):]
            if not os.path.exists(folder_dest):
                os.makedirs(folder_dest)
            
            if root == source and file in ["boot.py", "main.py", "config.py"] :
                shutil.copy(file_path, folder_dest)
            if file == "__init__.py" :
                shutil.copy(file_path, folder_dest)
            if file.endswith(".mpy") :
                shutil.move(file_path, folder_dest)


if __name__ == "__main__":
    chemin_source = os.getcwd() + '\carte'
    chemin_dest   = os.getcwd() + '\carte_mpy'
    convert_py_into_mpy(chemin_source, chemin_dest)

