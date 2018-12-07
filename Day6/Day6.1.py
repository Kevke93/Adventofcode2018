with open("in_k.txt", "r") as f:
    inputs = [[int(k.rstrip("\n").split(",")[0]), int(k.rstrip("\n").split(",")[1])] for k in f.readlines()]

minX = min(inputs, key=lambda x: x[1])[1]
minY = min(inputs, key=lambda x: x[0])[0]
maxX = max(inputs, key=lambda x: x[1])[1]
maxY = max(inputs, key=lambda x: x[0])[0]

cordDict = {}

for xField in range(minY,maxX + 1):
    for yField in range(minY,maxY + 1):

        minDist = 10000
        tie = False
        id = -1
        for i in range(len(inputs)):
            y = inputs[i][0]
            x = inputs[i][1]

            if abs(xField - x) + abs(yField - y) < minDist:
                minDist = abs(xField - x) + abs(yField - y)
                id = i
                tie = False
            elif minDist == abs(xField - x) + abs(yField - y):
                tie = True
        if not (tie):

            if xField == 0 or xField == maxX or yField == 0 or yField == maxY:
                cordDict[id] = -10000
            elif id in cordDict.keys():
                cordDict[id] += 1
            else:
                cordDict[id] = 1
maxVal = 0
for value in cordDict.values():
    if value > maxVal:
        maxVal = value

print(maxVal)
