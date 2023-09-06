from handler import writeContent

import os

current = "data/fileTree"

def muchArgs():
    writeContent("Invalid number of arguments")

def cd(self, *args):
    arg = args[0]

    if len(args) != 1:
        muchArgs()
        return
    while arg.startswith(".."):
        arg.split("/").pop(0)
        arg = "/".join(arg)
        current.split("/").pop(-1)
        if not "/".join(current).startswith("data/fileTree"):
            writeContent("can't go back further")
            return
        else:
            current.split("/").pop(-1)
            current = "/".join(current)
        arg = current + arg

    try:
        writeContent(arg + ":\n" + "\n".join(os.listdir(arg)))
    except OSError:
        writeContent("couldn't find folder:\n" + arg)

def openFile(args):
    if len(args) != 1:
        muchArgs()
        return
    
    arg = args[0]

    if arg.startswith("..") or arg.startswith("/"):
        writeContent("invalid filename")
        return

    arg = current + "/" + arg
    print(arg)

    try:
        with open(arg, "r") as f:
            writeContent(f.read())
    
    except FileNotFoundError as e:
        writeContent("couldn't find file " + arg + "\n" + str(e))


run = {"cd":cd, "open":openFile}
