import sys
import threading
sys.path.append("/data")

import variables as v
import json

import tkinter as tk

from datetime import date,datetime
from os import listdir,remove

standard = {"name": None, "lastLine": None}

hours = datetime.now().hour
minutes = datetime.now().minute

def writeContent(content):

    with open("test.txt", "w") as f:

        f.write(content + "\n")
        cache = content.split("\n")
        v.lastLine = cache[len(cache) - 1]


def readAnswer():

    with open("test.txt", "r") as f:

        content = f.read().split("\n")
        for line in reversed(content):
            if line != "":
                if line == v.lastLine:
                    return
                else:
                    return line
        return


def openWindow():

    print("opening Window")

    global frame

    frame = tk.Tk()

    frame.title("controlls")
    frame.resizable(False, False)

    startButton = tk.Button(frame, text = "Start game", command = lambda: startGame("new"))
    startButton.pack()
    files = listdir("saves")
    for f in files:
        button = tk.Button(frame, text = "slot " + str(f), command = lambda f=f: startGame(f))
        button.pack()

    print("mainloop")
    frame.protocol("WM_DELETE_WINDOW", saveGame)
    frame.mainloop()


def startGame(saveslot):

    writeContent("loading...")
    if saveslot == "new":

        with open("saves/" + str(date.today()) + " " + str(hours) + ":" + str(minutes) + ".json", "w") as f:
            f.write(json.dumps(standard))
        v.data["gameRunning"] = True

    else:
        with open("saves/" + saveslot, "r") as save:

            try:
                data = json.loads(save.read())
                try:

                    v.data["name"] = data["name"]
                    v.data["lastLine"] = data["lastLine"]
                    v.data["gameRunning"] = True

                except None:
                    saveError(saveslot, save, "saveslot data is incomplete")

            except json.JSONDecodeError:
                saveError(saveslot, save, "saveslot was empty or currupted")

def onWindowClose():
    frame.destroy()
    saveGame()

def saveGame():
    with open("saves/" + str(date.today()) + " " + str(hours) + ":" + str(minutes) + ".json", "w") as f:
        f.write(json.dumps(v.data))


def saveError(saveslot, save, error):
    writeContent(error + "\n\ntype 'new' to start all over\nor type 'change' to use another save file?")

    while readAnswer() != "new" and readAnswer() != "change":
        pass

    if readAnswer() == "new":
        save.write(json.loads(standard))

    else:
        writeContent("restarting")
        remove("saves/" + saveslot)
        openWindow()

print("handler")

windowThread = threading.Thread(target=openWindow)
windowThread.start()