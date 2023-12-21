import os
import time
import platform
import urllib.request

def parentdir():
    try:
        parent_directory = os.path.normpath(os.path.join(os.getcwd(), ".."))
        os.chdir(parent_directory)
    except Exception as e:
        print(f"Erreur lors du changement de répertoire : {e}")

def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def maj():
    parentdir()
    parentdir()
    os.remove("launcher.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/launcher.py", "launcher.py")
    os.chdir("test")
    os.chdir("sys_apps")
    os.remove("cmd.py")
    os.remove("store.py")
    os.remove("file_manager.py")
    os.remove("maj.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/cmd.py", "cmd.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/store.py", "store.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/file_manager.py", "file_manager.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/maj.py", "maj.py")
    os.system("python maj.py")

maj()
