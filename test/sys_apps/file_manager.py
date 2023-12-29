from colorama import Fore
import os
import platform
import psutil

system = platform.system()
if system == "Windows":
    clear = "cls"
    directory = "dir"
elif system == "Linux":
    clear = "clear"
    directory = "ls"
else:
    clear = "erreur"

couleur = Fore.GREEN
command_colors = Fore.RED

linux_command = ("""
 ┌─[file manager 0.10.1]─[administrator system]─[~]
 └──╼[★]$>>> """)
win_command = os.getcwd() + ">>>"
direct = os.getcwd()

with open("save_local.txt", "r") as local:
    locat = local.read()
    loc = locat.splitlines()
    cd = loc[0]

loc_save = cd + "system\save_config.txt"

if os.path.exists(loc_save):
    with open(loc_save, "r") as file:
        info = file.read()
        savelist = info.splitlines()
        entry_save = savelist[0]

        if entry_save == ">>>":
            entry = ">>>"

        elif entry_save == "lin":
            entry = linux_command

        elif entry_save == "win":
            entry = win_command
else:
    entry = linux_command

def convert_bytes(num, suffix='o'):
    for unit in [' ',' K',' M',' G',' T',' P',' E',' Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def get_disk_space_info(path='.'):
    usage = psutil.disk_usage(path)
    total_space = usage.total
    free_space = usage.free
    used_space = total_space - free_space
    return total_space, used_space

def list_files(path='.'):
    file_list = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        size = os.path.getsize(item_path) if os.path.isfile(item_path) else 0
        size_str = convert_bytes(size)
        file_list.append((item, size_str))
    return file_list

def list_all_disks():
    # Utiliser psutil pour obtenir tous les disques, y compris ceux non montés
    partitions = psutil.disk_partitions(all=True)
    disks = [partition.device for partition in partitions]
    return disks

def print_file_manager():
    print("Disques disponibles:")
    drives = list_all_disks()
    if not drives:
        print("Aucun disque disponible.")
    else:
        for drive in drives:
            try:
                total, used = get_disk_space_info(drive)
                total_str = convert_bytes(total)
                used_str = convert_bytes(used)
                print(f"- {drive} (Total: {total_str}, Utilisé: {used_str})")
            except Exception as e:
                print(f"Erreur lors de la récupération des informations pour {drive}: {e}")

    print("\nListe des fichiers et dossiers dans '", direct, "' :")
    files = list_files()
    for file, size in files:
        print(f"- {file:<50} {size}")

def hall():
    print(couleur)
    os.system(clear)
    print("pour se deplacer faire 'ch' au lieu de 'cd'")
    print("pour supprimer un fichier ou un dossier faire 'rm' puis son nom")
    print("les nom ayant 0o sont des dossiers")
    print()
    print_file_manager()
    print()

hall()
while True:
    print(direct)
    command = input(command_colors + entry)

    if command == "close":
        os.system(clear)
        break

    elif command == "clear":
        hall()

    elif command == "ch..":
        hall()
        try:
            parent_directory = os.path.normpath(os.path.join(os.getcwd(), ".."))
            os.chdir(parent_directory)
            direct = os.getcwd()
            hall()
        except Exception as e:
            print(f"Erreur lors du changement de répertoire : {e}")

    elif command == "ch/":
        hall()
        try:
            # Obtient la racine du disque
            root_directory = os.path.abspath(os.sep)
            os.chdir(root_directory)
            direct = os.getcwd()
            hall()
        except Exception as e:
            print(f"Erreur lors du changement de répertoire : {e}")

    elif command.startswith("ch"):
        hall()
        _, path = command.split(" ", 1)
        path = path.strip()

        try:
            os.chdir(path)
            direct = os.getcwd()
            hall()
        except FileNotFoundError:
            print(f"Le répertoire '{path}' n'existe pas.")
        except Exception as e:
            print(f"Erreur lors du changement de répertoire : {e}")

    elif command.startswith("rm"):
        hall()
        _, path = command.split(" ", 1)
        path = path.strip()

        try:
            os.remove(path)
            print(f"{path} supprimé")
            hall()
        except FileNotFoundError:
            print(f"Le fichier '{path}' n'existe pas.")
        except Exception as e:
            print(f"Erreur lors de la suppression de {path}: {e}")

    elif command == command:
        hall()
        print("\n>>> " + command + "\n")
        os.system(command)
