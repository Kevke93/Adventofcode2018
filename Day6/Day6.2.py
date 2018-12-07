with open("in_k.txt", "r") as f:
    inputs = [[int(k.split(",")[0]), int(k.rstrip("\n").split(",")[1])] for k in f.readlines()]

minX = min(inputs, key=lambda x: x[1])[1]
minY = min(inputs, key=lambda x: x[0])[0]
maxX = max(inputs, key=lambda x: x[1])[1]
maxY = max(inputs, key=lambda x: x[0])[0]

counter = 0

for xField in range(minX, maxX + 1):
    yField = minY
    while yField < maxY + 1:
        sum = 0

        for i in range(len(inputs)):
            y = inputs[i][0]
            x = inputs[i][1]
            sum += abs(x - xField) + abs(y - yField)
            if sum > 10000:
                break

        rangeCounter = 2
        if sum <10000:
            counter+=1
            while 10000 > sum + len(inputs) * rangeCounter and yField+rangeCounter < maxY - 1:
                counter += 1
                rangeCounter += 1

        elif sum>10000:
            while 10000 < sum -len(inputs) * rangeCounter and yField+rangeCounter < maxY - 1:
                rangeCounter += 1
        yField += 1 + rangeCounter - 2

print(counter)


