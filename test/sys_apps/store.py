import os
import ssl
import socket
import urllib.request

def parentdir():
    try:
        parent_directory = os.path.normpath(os.path.join(os.getcwd(), ".."))
        os.chdir(parent_directory)
    except Exception as e:
        print(f"Erreur lors du changement de répertoire : {e}")

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

def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def maj():
    parentdir()
    parentdir()
    os.remove("launcher.py")
    os.remove("ES.py")
    os.remove("ES_setup.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/launcher.py", "launcher.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/test/ES.py", "ES.py")
    fetch_file("https://raw.githubusercontent.com/1ventorus/emergency-system/main/ES_setup.py", "ES_setup.py")
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

if connected:
    maj()
else:
    print("vous n'étes pas connecté")
