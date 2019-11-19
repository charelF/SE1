#import pickle

##database = []
##datafile = "database.data"



class VM:

    def __init__(self, name, pwd):
        self.home = Dir(name)
        self.name = name
        self.pwd = pwd

class Dir:

    def __init__(self, name):
        self.name = name
        self.content = []
        self.parent = None

    def __repr__(self):
        return self.name

    def ls(self, layer=0):
        for _ in range(layer): print("---", end="")
        print(self)
        layer +=1
        for element in self.content:
            element.ls(layer)

    def add(self, fileS):
        if isinstance(fileS, list):
            self.content.extend(fileS)
            for file in fileS:
                file.parent = self
        else:
            self.content.append(fileS)
            fileS.parent = self

    def delete(self):
        pass

    def write(self, name, content):
        for i in content:
            if i.name == name and isinstance(i, File):
                i.content += content
            if i.name == name and isinstance(i, File):
                print("cant write to dir")
            else:
                self.content.append(File(name))
                self.write(name, content)

    def get(self, name):
        if name == ".":
            return self
        if name == "..":
            if self.parent:
                return self.parent
            else:
                return self
        
        for element in self.content:
            if element.name == name:
                return element
        print("no such file found")

    


class File:

    def __init__(self, name):
        self.name = name
        self.content = ""
        self.parent = None

    def __repr__(self):
        return self.name

    def ls(self, layer=0):
        for _ in range(layer): print("---", end="")
        print(self)

    def write(self, content):
        self.content += content


def initiate():
    global database
    f = open(datafile, "rb")
    #database = pickle.load(f)
    f.close()

def terminate():
    global database
    f = open(datafile, "wb+")
    p#ickle.dump(dataset, f)
    f.close()

def login(name, pwd):
    global LoggedIn
    # check if credentials are ok
    LoggedIn = True
    # check if WM already exists, if not ask admin to create it
    return userMachines[name]

def createVM(name, pwd):
    if name in userMachines:
        return False
    else:
        userMachines[name] = VM(name, pwd)
        return True

def printPath(directory):
    if directory == None: return ""
    output = directory.name
    while directory.parent != None:
        output = directory.parent.name + "/" + output
        directory = directory.parent
    return output + "/  "





vm = None

cwd = None

home = None

SU = False
LoggedIn = False

userMachines = {}

# to be done by admin:
createVM("charel", "1234")
    
print("Please login with your credentials as follows: login USERNAME PASSWORD")
while True:
    print(printPath(cwd), end="")
    userinput = input().split(" ")
    cmd = userinput[0]
    args = userinput[1:]

    if cmd == "login":
        vm = login(*args)
        cwd = vm.home
        home = vm.home

    
    if cmd == "mkdir":
        cwd.add(Dir(*args))

    if cmd == "mkfile":
        cwd.add(File(*args))

    if cmd == "ls":
        cwd.ls()

    if cmd == "write":
        cwd.write()

    if cmd == "cd":
        cwd = cwd.get(*args)
                    
        
        

    
    
main()

def debug():
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
    


