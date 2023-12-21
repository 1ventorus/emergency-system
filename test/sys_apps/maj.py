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
    locat=os.getcwd()
    os.remove("launcher.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/launcher.py?token=GHSAT0AAAAAACJJREYIVHLO6RRTCFZRILQQZMEVQ5Q", "launcher.py")
    os.chdir("test")
    location=os.getcwd()
    os.chdir("sys_apps")
    os.remove("cmd.py")
    os.remove("store.py")
    os.remove("file_manager.py")
    os.remove("maj.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/cmd.py?token=GHSAT0AAAAAACJJREYJ4DFGRLAT4USUOPBCZMEV6CA", "cmd.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/store.py?token=GHSAT0AAAAAACJJREYIH2L2JJ34QTDZP2XSZMEV6RA", "store.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/sys_apps/file_manager.py?token=GHSAT0AAAAAACJJREYJD7N6GL4TV4A7LJW2ZMEV6IQ", "file_manager.py")
    fetch_file