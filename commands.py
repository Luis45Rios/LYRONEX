import os
import time
import webbrowser
from datetime import datetime

# Abrir Brave
def open_brave():
    os.system("start brave")

# Abrir Spotify
def open_spotify():
    os.system("start spotify")

# Abrir Visual Studio Code
def open_VSCode():
    os.startfile(r"C:/Users/Luis/AppData/Local/Programs/Microsoft VS Code/Code.exe")

def hour():
    hora_actual = datetime.now().strftime("%H:%M %p")
    return hora_actual

def open_youtube():
    url = "https://www.youtube.com/"
    webbrowser.open(url)