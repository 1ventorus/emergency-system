import os
import time
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

def install():
    locat=os.getcwd()
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/launcher.py", "launcher.py")
    os.mkdir(os.path.join(locat, "test"))
    os.chdir("test")
    location=os.getcwd()
    os.mkdir(os.path.join(location, "sys_apps"))
    os.chdir("sys_apps")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/cmd.py", "cmd.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/store.py", "store.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/file_manager.py", "file_manager.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/maj.py", "maj.py")
    os.chdir(location)
    os.mkdir(os.path.join("system"))
    os.mkdir(os.path.join("programs"))
    os.mkdir(os.path.join("programs", "games"))
    os.mkdir(os.path.join("programs", "tool"))
    os.chdir(os.path.join("programs", "tool"))
    fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_setup.py", "toolbox_setup.py")
    os.chdir(locat)



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
            install()
        else:
            print("vous posséder déjà ES")
    elif launch=="n":
        os.system(clear)
        break
