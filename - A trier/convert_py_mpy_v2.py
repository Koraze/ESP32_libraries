import os
import mpy_cross
import subprocess
import shutil
from time import sleep

# Fonction copie dossier
def copy_directory(source, destination):
    try:
        shutil.copytree(source, destination)
        print("Dossier copié avec succès !")
        return True
    except :
        return False


def convert_py_into_mpy(source, dest):
    print("creating mpy destination folder")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    
    print("Copying folder")
    copy_directory(source, dest)
    
    print("creating mpy files")
    for root, dirs, files in os.walk(dest):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if root == dest and file in ["boot.py", "main.py", "config.py"] :
                pass
            elif file != "__init__.py" and file.endswith(".py") :
                file_path = os.path.join(root, file)
                mpy_cross.run(file_path, stdout=subprocess.PIPE).wait()
                os.remove(file_path)


if __name__ == "__main__":
    chemin_source = os.getcwd() + '\carte'
    chemin_dest   = os.getcwd() + '\carte_mpy'
    convert_py_into_mpy(chemin_source, chemin_dest)

