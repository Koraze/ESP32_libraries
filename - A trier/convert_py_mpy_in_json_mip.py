import json
import re
import os
import fileinput
import shutil


# Fonction pour remplacer récursivement dans toutes les chaînes
def remplacer_sous_chaines(donnees, ancien, nouveau):
    if isinstance(donnees, str):
        return re.sub(ancien, nouveau, donnees)
    elif isinstance(donnees, dict):
        return {k: remplacer_sous_chaines(v, ancien, nouveau) for k, v in donnees.items()}
    elif isinstance(donnees, list):
        return [remplacer_sous_chaines(v, ancien, nouveau) for v in donnees]
    else:
        return donnees

# Fonction copie dossier
def copy_directory(source, destination):
    try:
        shutil.copytree(source, destination)
        print("Dossier copié avec succès !")
        return True
    except :
        return False


def convert_json_into_mpy(source, dest):
    print("creating mpy destination folder")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    
    print("Copying folder")
    copy_directory(source, dest)

    print("creating mpy files")
    for root, dirs, files in os.walk(dest):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith(".json") :
                file_path   = os.path.join(root, file)
                print(file)
                with open(file_path, 'r', encoding='utf-8') as file_open:
                    contenu = json.load(file_open)
                    if "urls" in contenu :
                        for i in range(len(contenu["urls"])) :
                            if contenu["urls"][i][0].endswith(".py") :
                                contenu["urls"][i][1] = "github:Koraze/ESP32_librairies/carte_mpy/lib_/" + contenu["urls"][i][0]
                                if not contenu["urls"][i][0].endswith("__init__.py") :
                                    contenu["urls"][i][0] = contenu["urls"][i][0][:-2] + "mpy"
                                    contenu["urls"][i][1] = contenu["urls"][i][1][:-2] + "mpy"
                                # contenu["urls"] = remplacer_sous_chaines(contenu["urls"])
                                # print(json.dumps(contenu))
                    if "deps" in contenu :
                        contenu["deps"] = remplacer_sous_chaines(contenu["deps"], ancien='mip', nouveau='mip_mpy')
                        
                with open(file_path, 'w', encoding='utf-8') as file_open:
                    json.dump(contenu, file_open, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    chemin_source = os.getcwd() + '\mip'
    chemin_dest   = os.getcwd() + '\mip_mpy'
    convert_json_into_mpy(chemin_source, chemin_dest)

