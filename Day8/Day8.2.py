def sumTree(inputs):
    children, metaDa = next(inputs), next(inputs)

    if children == 0:
        result = 0
        for _ in range(metaDa):
            result += next(inputs)
        return result

    allSum = [sumTree(inputs) for _ in range(children)]
    currentMetda = [next(inputs) for _ in range(metaDa)]

    return sum(allSum[i - 1] for i in currentMetda if i <= len(allSum))


with open("in_k.txt", "r") as f:
    inputs = iter([int(x) for x in f.readline().split()])
print(sumTree(inputs))
