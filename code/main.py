import sys
import threading
sys.path.append("data")

import variables as v
import commands as c

from handler import writeContent, readAnswer

from time import sleep

answer = None
args = None
command = None
list = c.run

print("starting")
while not v.data["gameRunning"]:
    sleep(0.5)
    pass

print("game started")
writeContent("Hello, thank you for choosing this game\nit is all playing inside a text document...\nif you haven't noticed yet\n\nlets get started\nto confirm your answer just save the file with Ctrl + S\n\nwhat's your name?")

def setAnswer():
    global answer
    global args
    global command

    while v.data["gameRunning"]:
        if readAnswer() is not None:
            answer = readAnswer()
            args = answer.split(" ")
            command = args[0]
        #try:
        if answer is not None:
            if len(args) > 1:
                args.pop(0)
                print(args)
                list[command](args)
                answer = None
        #except ValueError as e:
        #    print("error:" + str(e))
        #    pass
        sleep(1)

def loop():
    print("gameloop")
    while True:
        if not v.data["gameRunning"]:
            sys.exit(0)


gameThread = threading.Thread(target=loop)
gameThread.start()

answerThread = threading.Thread(target=setAnswer)
answerThread.start()