from colorama import *
import os
import time
import getpass
import shutil
import platform

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

system = platform.system()
if system=="Windows":
    clear="cls"
elif system =="Linux":
    clear ="clear"
else:
    clear ="erreur"

couleur = Fore.GREEN
command_colors = Fore.RED
local=os.getcwd()
def hall():
    os.system(clear)
    print(couleur + BANNER)

def create_user_directory(user, password):
    local1 = os.getcwd()
    user_path = os.path.join(local1, user)
    
    if not os.path.exists(user_path):
        os.mkdir(user_path)
        
        # Copier ES.py dans le répertoire de l'utilisateur
        shutil.copy(os.path.join(local1, "test", "ES.py"), user_path)
        print("ES.py copié avec succès.")

        # Créer le répertoire sys_apps et copier les fichiers de référence
        sys_apps_path = os.path.join(user_path, "sys_apps")
        os.mkdir(sys_apps_path)
        shutil.copy(os.path.join(local1, "test", "sys_apps", "cmd.py"), sys_apps_path)
        print("cmd.py copié avec succès.")
        shutil.copy(os.path.join(local1, "test", "sys_apps", "store.py"), sys_apps_path)
        print("store.py copié avec succès.")

        # Créer les répertoires system, programs, games et tool
        os.mkdir(os.path.join(user_path, "system"))
        os.mkdir(os.path.join(user_path, "programs"))
        os.mkdir(os.path.join(user_path, "programs", "games"))
        os.mkdir(os.path.join(user_path, "programs", "tool"))

        # Écrire les informations de connexion dans logs.txt
        with open(os.path.join(user_path, "system", "logs.txt"), "w+") as logs:
            logs.write(user + "\n" + password)
        print("Logs.txt créé avec succès.")

def launch():
    load=1
    if load !=5:
            load =+1
            os.system(clear)
            print("chargement")
            time.sleep(0.5)
            os.system(clear)
            print("chargement.")
            time.sleep(0.5)
            os.system(clear)
            print("chargement..")
            time.sleep(0.5)
            os.system(clear)
            print("chargement...")
            time.sleep(0.5)
    load =-4

def loading():
    launch()
    os.system(clear)

def close():
    load3=1
    if load3 !=5:
            load =+1
            os.system(clear)
            print("fermeture")
            time.sleep(0.5)
            os.system(clear)
            print("fermeture.")
            time.sleep(0.5)
            os.system(clear)
            print("fermeture..")
            time.sleep(0.5)
            os.system(clear)
            print("fermeture...")
            time.sleep(0.5)
    load3 =-4

def closing():
    close()
    print(Style.RESET_ALL)
    close()
    os.system(clear)

loading()
print(couleur)
loading()

while True:
    os.chdir(local)
    hall()
    print("entrez votre nom d'utilisateur ou close pour quitter")
    print()
    user = input(command_colors + ">>>")
    print(couleur)
    os.system(clear)
    if user == "close":
        closing()
        os.system(clear)
        print("au revoir !")
        time.sleep(2)
        os.system(clear)
        break
    else:
        hall()
        print("entrez votre mot de passe")
        print()
        password = getpass.getpass(command_colors + ">>>")
        print(couleur)

        create_user_directory(user, password)
        os.chdir(user)
        os.system("python ES.py")
        hall()
