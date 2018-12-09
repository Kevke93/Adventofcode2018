with open("in_k.txt", "r") as f:
    inputs = iter([int(x) for x in f.readline().split()])

stack = []
res = 0
newNode = True

while 1:
    if newNode:
        children, metaDa = next(inputs), next(inputs)
        if children == 0:
            stack.append((0, metaDa))
            newNode = False
        else:
            stack.append((children - 1, metaDa))
    else:
        if len(stack) == 0:
            break
        children, metaDa = stack.pop()
        if children == 0:
            for _ in range(metaDa):
                res += next(inputs)
            newNode = False
        else:
            stack.append((children - 1, metaDa))
            newNode = True
print(res)
