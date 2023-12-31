import os
import ssl
import socket
import platform
import urllib.request

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
  ┌─┐┌─┐┌┬┐┬ ┬┌─┐
  └─┐├┤  │ │ │├─┘
  └─┘└─┘ ┴ └─┘┴  
 """)

system = platform.system()
if system=="Windows":
    clear="cls"
elif system =="Linux":
    clear ="clear"
else:
    clear ="erreur"

Help = ("""
 installer emergency system : 
 suivez les consignes et tout se passera bien
 toolbox s'installe au meme emplacement que ES_setup
 avec tout les requierments

""")

def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 443))
        context = ssl.create_default_context()
        with socket.create_connection(("www.google.com", 443)) as sock:
            with context.wrap_socket(sock, server_hostname="www.google.com") as ssock:
                return True, ssock.version()
    except OSError:
        return False, None
connected, ssl_version = check_internet_connection()

def install():
    locat = os.getcwd()

    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/launcher.py", "launcher.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/ES.py", "ES.py")
    os.system("pip install colorama")
    os.system("pip install psutil")
    test_dir = os.path.join(locat, "test")
    if not os.path.exists(test_dir):
        os.mkdir(test_dir)
        os.chdir(test_dir)
        sys_apps_dir = os.path.join(test_dir, "sys_apps")
        os.mkdir(sys_apps_dir)
        os.chdir(sys_apps_dir)
        fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/cmd.py", "cmd.py")
        fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/store.py", "store.py")
        fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/file_manager.py", "file_manager.py")
        fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/maj.py", "maj.py")
        os.chdir(test_dir)
        system_dir = os.path.join("system")
        os.mkdir(system_dir)
        programs_dir = os.path.join("programs")
        os.mkdir(programs_dir)
        games_dir = os.path.join(programs_dir, "games")
        os.mkdir(games_dir)
        tool_dir = os.path.join(programs_dir, "tool")
        os.mkdir(tool_dir)
        os.chdir(tool_dir)
        fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_setup.py", "toolbox_setup.py")
        os.chdir(locat)
        print("installation terminé")
        print("vous pouvez fermer l'installateur")



def hall():
    os.system(clear)
    print(BANNER)
    print(Help)
    print("lancer l'installation de ES o/n ou y/n")

hall()
while True:
    launch=input(">>>")

    if launch=="o" or launch=="y":
        hall()
        if not os.path.exists("test"):
            if connected:
                install()
            else:
                print("vous n'étes pas connecté")
        else:
            print("vous posséder déjà ES")
    elif launch=="n":
        os.system(clear)
        break
