
class VM:

    def __init__(self, name):
        self.home = Dir(name)

class Dir:

    def __init__(self, name):
        self.name = name
        self.content = []

    def __repr__(self):
        return self.name

    def ls(self, layer=0):
        for _ in range(layer): print("---", end="")
        print(self)
        layer +=1
        for element in self.content:
            element.ls(layer)
        


class File:

    def __init__(self, name):
        self.name = name
        self.content = ""

    def __repr__(self):
        return self.name

    def ls(self, layer=0):
        for _ in range(layer): print("---", end="")
        print(self)


def main():
    vm = VM("charel")
    f1 = File("file1")
    f2 = File("file2")
    f3 = File("file3")

    d1 = Dir("dir1")
    d2 = Dir("dir2")
    d3 = Dir("dir3")

    vm.home.content.extend([f1, d1, f2])
    d2.content.extend([d3, f3])
    d1.content.append(d2)

    vm.home.ls()
main()

    



##
##
##def initiate():
##    # the user logs in, and if succesful and if ActUser,
##    #receives the base directory of its VM
##
##def createUserDirectory(user):
####    if isSU:
####        homeDir
##    print("create user directory")
##
##def readFile(name):
##    print("readFile")
##
##
##def main():
##
##    command =  input()
##
##    if command == "start":
##        initiate()
##
##    if command == "ls":
##        print("not implemented")
##
##    if command == "mkfile":
##        
##        
##
##
##    if command == "stop":
##        terminate()
##
##    

    
