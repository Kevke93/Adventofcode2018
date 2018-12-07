import time as t


class Node:

    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
        self.duration = 60 + (ord(name) - ord("A") + 1)

    def addParent(self, otherNode):
        if not (otherNode in self.parents):
            self.parents.append(otherNode)

    def addChid(self, otherNode):
        if not (otherNode in self.children):
            self.children.append(otherNode)


def findNext(toDoList, doneList):
    nextNode = None
    for node in toDoList:
        allParentsDone = True
        for parent in node.parents:

            if not (parent in doneList):
                allParentsDone = False
                break

        if nextNode == None:
            if allParentsDone:
                nextNode = node
        elif node.name < nextNode.name and allParentsDone:
            nextNode = node

    return nextNode


def minTime(inProgressSet):
    minJob = 200
    for x in inProgessSet:
        if x.duration < minJob:
            minJob = x.duration
    return minJob


with open("in_k.txt", 'r') as f:
    inputs = [[line[5], line[36]] for line in f.readlines()]

start = t.perf_counter()
allNode = {}
for pair in inputs:

    if not (pair[0] in allNode):
        allNode[pair[0]] = Node(pair[0])
    if not (pair[1] in allNode):
        allNode[pair[1]] = Node(pair[1])
    allNode[pair[1]].addParent(allNode[pair[0]])
    allNode[pair[0]].addChid(allNode[pair[1]])

# find the ones with no partens
toDoSet = set()

for node in allNode.values():
    if len(node.parents) == 0:
        toDoSet.add(node)

doneSet = set()
inProgessSet = set()
time = 0

while len(allNode) != len(doneSet):

    while len(inProgessSet) < 5:
        nextElement = findNext(toDoSet, doneSet)

        if nextElement == None:
            break
        inProgessSet.add(nextElement)
        toDoSet.remove(nextElement)

    deltaTime = minTime(inProgessSet)
    time += deltaTime

    # update:
    removeList = []
    for x in inProgessSet:
        x.duration -= deltaTime
        if x.duration == 0:
            doneSet.add(x)
            removeList.append(x)
            toDoSet |= set(x.children)
    for x in removeList:
        inProgessSet.remove(x)

print(time)
print(t.perf_counter())
