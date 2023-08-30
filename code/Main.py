import data
from time import sleep

def writeContent(content):

    with open("test.txt", "w") as f:

        f.write(content)
        cache = content.split("\n")
        data.lastLine = cache[len(cache) - 1]

def readAnswer():

    with open("test.txt", "r") as f:

        content = f.read().split("\n")
        for line in reversed(content):
            if line != "":
                if line == data.lastLine:
                    return
                else:
                    return line
        return

writeContent("test\nlol")
while True:
    print(readAnswer())
    sleep(1)