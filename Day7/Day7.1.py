class Node:

    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []

    def addParent(self, otherNode):
        if not (otherNode in self.parents):
            self.parents.append(otherNode)

    def addChid(self, otherNode):
        if not (otherNode in self.children):
            self.children.append(otherNode)


def findNext(toDoSet, doneSet):
    nextNode = None
    for node in toDoSet:
        allParentsDone = True
        for parent in node.parents:

            if not (parent in doneSet):
                allParentsDone = False

        if nextNode == None:
            if allParentsDone:
                nextNode = node
        elif node.name < nextNode.name and allParentsDone:
            nextNode = node

    return nextNode


with open("in_k.txt", 'r') as f:
    inputs = [[line[5], line[36]] for line in f.readlines()]

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
out = ""
while len(toDoSet) != 0:
    nextElement = findNext(toDoSet, doneSet)

    toDoSet |= set(nextElement.children)
    toDoSet.remove(nextElement)
    doneSet.add(nextElement)

    out += nextElement.name

print(out)
