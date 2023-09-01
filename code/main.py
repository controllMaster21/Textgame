import sys
sys.path.append("data")

import variables as v

from handler import *

from time import sleep

print("Vor dem Start von startGame:", v.data["gameRunning"])
startGame("new")
print("Nach dem Start von startGame:", v.data["gameRunning"])

while not v.data["gameRunning"]:
    sleep(0.5)
    pass

writeContent("Hello, thank you for choosing this game\nit is all playing inside a text document...\nif you haven't noticed yet\n\nlets get started\nto confirm your answer just save the file with Ctrl + S\n\nwhat's your name?")
openWindow()

while v.data["gameRunning"]:
    while True:
        answer = readAnswer()
        if answer is not None:
            break

    v.data["name"] = readAnswer()
    print(v.data["name"])
    sleep(1)

