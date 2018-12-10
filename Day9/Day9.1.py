from collections import defaultdict, deque

with open("in_k.txt", "r") as f:
    inputs = f.readline().split()

players, lastMarb = int(inputs[0]), int(inputs[6])

standings = defaultdict(int)
field = deque()
field.append(0)

for marble in range(1, lastMarb + 1):
    # The new marble should always be inserted at the last position, makes it easy to acess

    if marble % 23 != 0:
        field.rotate(-1)
        field.append(marble)
    else:
        field.rotate(7)
        standings[marble % players ] += marble + field.pop()
        field.rotate(-1)

print(max(standings.values()))
