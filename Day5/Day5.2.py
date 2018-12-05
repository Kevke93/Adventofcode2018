with open("in_k.txt", 'r') as f:
    standardInputs = f.readline()

shortestString = 10000

for i in range(65,91):

    inputs = standardInputs.replace(chr(i), "").replace(chr(i+32),"")
    counter = 0

    while counter < len(inputs) - 2:
        if abs(ord(inputs[counter]) - ord(inputs[counter + 1])) == 32:
            inputs = inputs.replace(inputs[counter:counter + 2], "")
            if counter > 0:
                counter +=-1
        else:
            counter += 1

    if len(inputs) < shortestString:
        shortestString = len(inputs)
print(shortestString)

