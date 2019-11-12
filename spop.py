# I am sorry for not having a lot of code as of this point in time
# I had to change programming language due to technical difficulties

import json

isAuthenticated = False
isSU = False

def initiate():
    global homeDirFile
    global homeDir
    global isAuthenticated
    global isSU

    homeDirFile = open("fileSystem.txt", w+)
    homeDir = json.load(homeDirFile)

def createUserDirectory(user):
##    if isSU:
##        homeDir
    print("create user directory")

def readFile(name):
    print("readFile")


def main():

    command =  input()

    if command = "start":
        initiate()

    if command = "ls":
        readFile()


    if command = "stop":
        terminate()

    

    
