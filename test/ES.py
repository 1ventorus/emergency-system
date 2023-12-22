
# import
from colorama import*

import os
import time
import socket
import uuid
import platform
import psutil
import ssl


# affichage
BANNER =("""
 ######## ##     ## ######## ########   ######   ######## ##    ##  ######  ##    ## 
 ##       ###   ### ##       ##     ## ##    ##  ##       ###   ## ##    ##  ##  ##  
 ##       #### #### ##       ##     ## ##        ##       ####  ## ##         ####   
 ######   ## ### ## ######   ########  ##   #### ######   ## ## ## ##          ##    
 ##       ##     ## ##       ##   ##   ##    ##  ##       ##  #### ##          ##    
 ##       ##     ## ##       ##    ##  ##    ##  ##       ##   ### ##    ##    ##    
 ######## ##     ## ######## ##     ##  ######   ######## ##    ##  ######     ##    
  ######  ##    ##  ######  ######## ######## ##     ##                              
 ##    ##  ##  ##  ##    ##    ##    ##       ###   ###                              
 ##         ####   ##          ##    ##       #### ####                              
  ######     ##     ######     ##    ######   ## ### ##                              
       ##    ##          ##    ##    ##       ##     ##                              
 ##    ##    ##    ##    ##    ##    ##       ##     ##                              
  ######     ##     ######     ##    ######## ##     ##                              
 """)

BANNER2 =("""
  ____>>>ES/<<<____________________________________________________
 |       toutes les commandes d'info du cmd fonctionnent !         |
 |                                                                 |
 | parametre : affiche les paramètres                              |
 | IPinfo : donne toute les info ip de la machine                  |
 | MACinfo : donne toute les info MAC de la machine                |
 | aide : affiche plus de commande                                 |
 | clear : même fonction que 'cls' mais garde l'interface          |
 | save : sauvegarde les paramètres actuel                         |
 | load : charge les dernier paramètre sauvegardé                  |
 | close : ferme le système de sécurité d'urgence                  |
 |_________________________________________________________________|
 """)

aide = ("""
  ____>>>ES/aide<<<________________________________________________________
 |           toute les commandes d'info du cmd fonctionnent !              |
 |                                                                         |
 | parametre : affiche les paramètres                                      |
 | chat : permet de discuter avec soi même                                 |
 | IPinfo : donne toute les info ip de la machine                          |
 | MACinfo : donne toute les info MAC de la machine                        |
 | os : donne le systeme d'exploitation (os) de la machine                 |
 | info sys : donne les info sur le systeme physique                       |
 | defend no : désactive windows defender                                  |
 | defend yes : active windows defender                                    |
 | internet : verifie la connexion internet                                |
 | ipconfig : donne les info sur le materiel                               |
 | chdir : permet de se deplacer dans un répertoire précis                 |
 | curl ipinfo.io : donne l'adrese ip public                               |  
 | clear : même fonction que 'cls' mais garde l'interface                  |
 | ch 'chemin' : se déplace au chemin indiqué                              |
 | ch/ : revient a la racine du disque                                     |
 | ch.. : revient au dossier précedent                                     |
 | save : sauvegarde les paramètres actuel                                 |
 | load : charge les dernier paramètre sauvegardé                          |
 | credits : affiche les credits ainsi que la version de toolbox           |
 | close : ferme le cmd personnalisé                                       |
 |_________________________________________________________________________| 
 """)

gen_parameters=("""
  ____>>>ES/paramètres<<<__________________________________________________
 |                                                                         |
 | commande : accede au parametre des commandes                            |
 | info : donne les toute les info de ES                                   |
 | close : retourne dans ES                                                |
 |_________________________________________________________________________|
 """)

command_sys=("""
  ____>>>ES/paramètres/commande<<<_________________________________________
 |                                                                         |
 | linux : modifie le texte de commande pour celui de linux                |
 | win : modifie le texte de commande pour celui de windows                |
 | defaut : modifie le texte de commande pour celui par défaut de ES       |
 | close : retourne au parametre generaux                                  |
 |_________________________________________________________________________|
 """)

apps=("""
  ____>>>ES/apps<<<________________________________________________________
 |                                    |                                    |
 | outils :                           | microsoft :                        |
 |      -toolbox                      |      -powerpoint                   |
 |      -cmd                          |      -word                         |
 |      -file manager (fm)            |      -excel                        |
 |      -store                        |                                    |
 |                                    |                                    |
 | apps :                             | jeux :                             |
 |      -                             |       -life evol                   |
 |      -                             |       -nuclear ingenior (ni)       |
 |      -                             |       -                            |
 |      -                             |       -                            |
 |      -                             |       -                            |
 |      -                             |       -                            |
 |      -                             |       -                            |
 |      -                             |       -                            |
 |_________________________________________________________________________|
 
 """)

cred=("""
 credits : 
  conception : 1ventorus

 merci de me contacter pour plus d'info au adresse mail suivante
    personnel :
      1ventorus@gmail.com
    
    professionel :
      x.storm.group@gmail.com

 """)

new=("""
 version actuel de ES :
    beta 0.10.1
 
 dernier ajout :
    -lancement d'application
 """)

# systeme de commande
linux_command=("""
 ┌─[ES 0.10.1]─[administrator system]─[~]
 └──╼[★]$>>> """)
win_command=os.getcwd() + ">>>"       # os.getcwd() permet d'obtenir la position sous format str 

# variable d'environnement
system = platform.system()
if system=="Windows":
    clear="cls"
elif system =="Linux":
    clear ="clear"
else:
    clear ="erreur"
couleur = Fore.GREEN
command_colors = Fore.RED
entry_com="lin"
entry=linux_command
location=os.getcwd()

# fonction complex
def save_config():
    with open("system\save_config.txt", "w+") as fichier:
        if entry_com == "win":
            entry_save = "win"

        elif entry_com == "lin":
            entry_save = "lin"

        elif entry_com == "defaut":
            entry_save = ">>>"

        fichier.write(entry_save)
        fichier.close()

def save_local():
    cd=os.getcwd()
    with open("sys_apps\save_local.txt", "w+") as local:
        local.write(cd)
        local.close()


def hall():
    os.system(clear)
    print(couleur + BANNER)
    print(couleur + BANNER2)
    print("vous êtes acutellement sur le disque :\n")
    os.system("cd")
    print()

def General_Parameters():
    os.system(clear)
    print(couleur + BANNER)
    print(couleur + gen_parameters)
    print()

def Command_Parameters():
    os.system(clear)
    print(couleur + BANNER)
    print(couleur + command_sys)
    print()


def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 443))
        context = ssl.create_default_context()
        with socket.create_connection(("www.google.com", 443)) as sock:
            with context.wrap_socket(sock, server_hostname="www.google.com") as ssock:
                return True, ssock.version()
    except OSError:
        return False, None

def disable_windows_defender():
    os.system("powershell -command Set-MpPreference -DisableRealtimeMonitoring 1")

def enable_windows_defender():
    os.system("powershell -command Set-MpPreference -DisableRealtimeMonitoring 0")

def get_ipv4_address():
    # Obtention de l'adresse IPv4
    ip = socket.gethostbyname(socket.gethostname())
    return ip

def get_ipv6_address():
    # Obtention de l'adresse IPv6
    ip = [l for l in ([ip for ip in socket.getaddrinfo(socket.gethostname(), None) if ':' in ip[4][0]]) if l]
    return ip[0][4][0] if ip else None

def get_mac_address():
    # Obtention de l'adresse MAC
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1])
    return mac

def get_system_info():
    # Informations de base sur la plate-forme
    system_info = {
        "système d'exploitation": platform.system(),
        "Nom de la machine": platform.node(),
        "nom de version": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processeur": platform.processor(),
    }

    print("Informations général du système:")
    for key, value in system_info.items():
        print(f"{key}: {value}")
    print("\n")

    print("Informations sur la mémoire:")
    # Informations sur la mémoire
    memory_info = psutil.virtual_memory()
    print(f"Mémoire totale: {memory_info.total / (1024 ** 3):.2f} GB")
    print(f"Mémoire utilisée: {memory_info.used / (1024 ** 3):.2f} GB")
    print("\n")

    # Informations sur le processeur
    print("info du processeur:")
    print(f"Modèle du processeur: {platform.processor()}")
    print(f"Nombre de cœurs physiques: {psutil.cpu_count(logical=False)}")
    print(f"Nombre de threads logiques: {psutil.cpu_count(logical=True)}")
    print("\n")

    # Utilisation du CPU
    print("Utilisation du processeur par cœur:")
    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
    for i, core_usage in enumerate(cpu_usage, 1):
        print(f"Cœur {i}: {core_usage}%")
    print("\n")

    # Informations sur les disques
    disk_info = psutil.disk_partitions()
    print("Informations sur les disques:")
    for disk in disk_info:
        print(f"Disque {disk.device}:")
        print(f"  Type: {disk.fstype}")
        print(f"  Espace total: {psutil.disk_usage(disk.device).total / (1024 ** 3):.2f} GB")
        print(f"  Espace utilisé: {psutil.disk_usage(disk.device).used / (1024 ** 3):.2f} GB")


# variable d'association
ipv4 =get_ipv4_address()
ipv6 =get_ipv6_address()
mac_adress =get_mac_address()
connected, ssl_version = check_internet_connection()


# initialisation
if os.path.exists(r"system\save_config.txt"):
    with open(r"system\save_config.txt", "r") as file:
        info = file.read()
        savelist = info.splitlines()
        entry_save = savelist[0]

        if entry_save == ">>>":
            entry = ">>>"

        elif entry_save == "lin":
            entry = linux_command

        elif entry_save == "win":
            entry = win_command

        
local1=os.getcwd()
hall()

# programme
while True:
    command =input(command_colors + entry)
    print(couleur)

 # parametre
    if command =="parametre":
        General_Parameters()
        while True:
            control = input(command_colors + entry)
    # parametre de l'entré des commande
            if control=="commande":
                Command_Parameters()
                while True:
                    command_system = input(command_colors + entry)

         # style visuel commande
                    if command_system=="linux":
                                entry= linux_command
                                entry_com = "lin"

                    elif command_system=="win":
                                entry= win_command
                                entry_com = "win"

                    elif command_system=="defaut":
                                entry= ">>> "
                                entry_com = "defaut"

         # retour au parametre généraux
                    elif command_system=="close":
                                General_Parameters()
                                break

                    else:
                                print("veuillez recommencer")
                                time.sleep(2)
                    Command_Parameters()


        # info systeme
            elif control=="info":
                General_Parameters()
                print(couleur + new)

        # fermeture des parametre
            elif control=="close":
                        hall()
                        break

    # erreur
            else:
                        print("veuillez recommencer")
                        time.sleep(2)
                        General_Parameters()

  # ip info
    elif command =="IPinfo":
                hall()
                print(command_colors + "ip :\n\n ipv4 : ", ipv4, "\n ipv6 : ", ipv6)

  # mac info
    elif command =="MACinfo":
                hall()
                print(command_colors + "adresse MAC : \n\n", mac_adress)
                print()

        # os info
    elif command =="os":
        hall()
        system_name = os.name
                
        if system_name == "posix":
            print("système d'exploitation Unix")
            print("cette os correspond a toute les version de linux et macOS")
            unix_version = platform.uname()
            print("Informations sur la version d'Unix :", unix_version)
                
        elif system_name == "nt":
            print("système d'exploitation Windows")
            windows_version = platform.version()
            print("Version de Windows :", windows_version)
                
        else:
            print("Système d'exploitation non reconnu.")

        # systeme chat
    elif command =="chat":
        hall()
        while True:
                
            chat = input(couleur + "que voulez vous dire ? ")

            if chat == chat:
                hall()
                print(couleur + chat)

            if chat =="clear":
                hall()

            if chat =="exit":
                hall()
                break

        # info sur le systeme
    elif command =="info sys":
        hall()
        get_system_info()

        # verification d'internet
    elif command =="internet":
        hall()
        if connected:
            print("Le PC est connecté à Internet. 🌐")
            if ssl_version:
                print("La connexion est sécurisée avec la version:", ssl_version)
            else:
                print("La connexion n'est pas sécurisée. 🌐❌")
        else:
            print("Le PC n'est pas connecté à Internet. ❌")

        # windows defender
    elif command=="defend no":
        hall()
        disable_windows_defender()

    elif command=="defend yes":
        hall()
        enable_windows_defender()

        # help
    elif command =="aide":
        os.system(clear)
        print(couleur + BANNER)
        print(couleur + aide)

        # clear
    elif command =="clear":
        hall()

        # systeme d'apps
    elif command =="apps":
        os.system(clear)
        print(BANNER)
        print(apps)

    # extinction systeme
    elif command =="close":
        save_config()
        os.system(clear)
        break

    elif command =="vs code":
        if os.path.exists(r"C:\Program Files\vs code\Microsoft VS Code"):
            hall()
            local=os.getcwd()
            os.chdir("C:")
            os.chdir(r"C:\Program Files\vs code\Microsoft VS Code")
            os.system("Code.exe")
            os.chdir(local)
            hall()

    elif command =="powerpoint":
        if os.path.exists(r"C:\Program Files\Microsoft Office\root\Office16"):
            hall()
            local=os.getcwd()
            os.chdir("C:")
            os.chdir(r"C:\Program Files\Microsoft Office\root\Office16")
            os.system("POWERPNT.EXE")
            os.chdir(local)
            hall()

    elif command =="word":
        if os.path.exists(r"C:\Program Files\Microsoft Office\root\Office16"):
            hall()
            local=os.getcwd()
            os.chdir("C:")
            os.chdir(r"C:\Program Files\Microsoft Office\root\Office16")
            os.system("WINWORD.EXE")
            os.chdir(local)
            hall()

    elif command =="excel":
        if os.path.exists(r"C:\Program Files\Microsoft Office\root\Office16"):
                hall()
                local=os.getcwd()
                os.chdir("C:")
                os.chdir(r"C:\Program Files\Microsoft Office\root\Office16")
                os.system("EXCEL.EXE")
                os.chdir(local)
                hall()

    elif command =="educadhoc":
        if os.path.exists(r"E:\livres\math\educadhoc"):
            hall()
            local=os.getcwd()
            os.chdir("E:")
            os.chdir(r"E:\livres\math\educadhoc")
            os.system("educadhoc.exe")
            os.chdir(local)
            hall()

    elif command =="cmd":
        hall()
        save_local()
        local=os.getcwd()
        os.chdir(location)
        os.chdir(r"sys_apps")
        os.system("python cmd.py")
        os.chdir(local)
        hall()

    elif command =="file manager" or command=="fm":
        hall()
        save_local()
        local=os.getcwd()
        os.chdir(location)
        os.chdir(r"sys_apps")
        os.system("python file_manager.py")
        os.chdir(local)
        hall()

    elif command =="toolbox":
        hall()
        local=os.getcwd()
        os.chdir(location)
        os.chdir(r"programs\tool\toolbox")
        if os.path.exists(r"programs\tool\toolbox\toolbox_w.py"):
            os.system("python toolbox_win.py")
        else:
            if os.path.exists(r"programs\tool\toolbox\toolbox_setup.py"):
                os.system("python toolbox_setup.py")
            else:
                print("toolbox n'est pas installé")
        os.chdir(local)
        hall()

    elif command =="life evol":
        hall()
        local=os.getcwd()
        os.chdir(location)
        os.chdir(r"programs\games")
        if os.path.exists(r"programs\games\life_evol.py"):
            os.system("python life_evol.py")
        else:
            if os.path.exists(r"programs\games\life_evol_setup.py"):
                os.system("python life_evol_setup.py")
            else:
                print("life evol n'est pas installé")
        os.chdir(local)
        hall()

    elif command =="nuclear ingenior" or command =="ni":
        hall()
        local=os.getcwd()
        os.chdir(location)
        os.chdir(r"programs\games\nuclear_ingenior.py")
        os.system("python nuclear_ingenior.py")
        os.chdir(local)
        hall()

    elif command =="store":
        save_local()
        hall()
        local=os.getcwd()
        os.chdir(location)
        os.chdir(r"sys_apps")
        os.system("python store.py")
        os.chdir(local)
        hall()

        # credits
    elif command =="credits":
        hall()
        print(couleur + cred)
        print("")

        # save des réglages
    elif command =="save":
        save_config()
        hall()
        print("paramètre sauvegardé")

    elif command =="load":
        os.chdir(local1)
        if os.path.exists(r"system\save_config.txt"):
            with open(r"system\save_config.txt", "r") as file:
                info = file.read()
                savelist = info.splitlines()
                entry_save = savelist[0]

                if entry_save == ">>>":
                    entry = ">>>"

                elif entry_save == "lin":
                    entry = linux_command

                elif entry_save == "win":
                    entry = win_command
                    
            hall()
            print("paramètre chargé")
        else:
            hall()
            print("vous n'avez aucune sauvegarde")

        # déplacment dans le pc
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

        # commande de cmd
    else:
        hall()
        print(command_colors + "\n>>> " + command + "\n")
        os.system(command)


# Récupérer le chemin absolu du répertoire contenant le script Python
# dir_path = os.path.dirname(os.path.realpath(__file__))
# Changer le répertoire de travail actuel vers le répertoire du script
# os.chdir(dir_path)
