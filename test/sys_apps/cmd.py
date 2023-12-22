from colorama import*

import os
import platform


system = platform.system()
if system=="Windows":
    clear="cls"
    directory="dir"
    ver=("windows version 0.10.1")
elif system =="Linux":
    clear ="clear"
    directory="ls"
    ver=("linux version 0.10.1")
else:
    clear ="erreur"

couleur = Fore.GREEN
command_colors = Fore.RED

def hall():
    os.system(clear)
    print(couleur)
    print(ver)
    print("")


linux_command=("""
 ┌─[CMD 0.10.1]─[administrator system]─[~]
 └──╼[★]$>>> """)
win_command=os.getcwd() + ">>>"

with open("save_local.txt", "r") as local:
    locat=local.read()
    loc=locat.splitlines()
    cd=loc[0]

loc_save =cd + "system\save_config.txt"

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

hall()
while True:
    command=input(command_colors + entry)

    if command =="close":
        os.system(clear)
        break

    elif command == "ch..":
        hall()
        try:
            parent_directory = os.path.normpath(os.path.join(os.getcwd(), ".."))
            os.chdir(parent_directory)
            hall()
        except Exception as e:
            print(f"Erreur lors du changement de répertoire : {e}")

    elif command == "ch/":
        hall()
        try:
            # Obtient la racine du disque
            root_directory = os.path.abspath(os.sep)
            os.chdir(root_directory)
            hall()
        except Exception as e:
            print(f"Erreur lors du changement de répertoire : {e}")

    elif command.startswith("ch"):
        hall()
        _, path = command.split(" ", 1)
        path = path.strip()

        try:
            os.chdir(path)
            print(f"Changement de répertoire vers : {path}")
            hall()
        except FileNotFoundError:
            print(f"Le répertoire '{path}' n'existe pas.")
        except Exception as e:
            print(f"Erreur lors du changement de répertoire : {e}")

    elif command == command:
        hall()
        print("\n>>> " + command + "\n")
        os.system(command)
