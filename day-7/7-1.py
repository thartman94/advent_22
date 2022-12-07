with open("./test.txt") as file:
    lines = file.readlines()

fileStructure = {"/": {}}
currentDir = fileStructure["/"]
fileStack = ["/"]


def changeDirectory(directory: str) -> None:
    if directory == "/":
        fileStack = ["/"]
    else:
        fileStack.append(directory)
        fileStructure[directory] = {}


def listItems() -> None:
    pass


def handleResponse(response: str) -> None:
    data = response.strip().split(" ")
    file = {"size": data[0], "name": data[1]}
    print(file)


for line in lines:
    data = line.strip().split(" ")
    if line[0] == "$":
        changeDirectory(line[2]) if line[1] == "cd" else listItems()
    else:
        handleResponse(line)
