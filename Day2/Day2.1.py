# A1
# To make sure you didn't miss any, you scan the likely candidate boxes again,
# counting the number that have an ID containing exactly two of any letter and
# then separately counting those with exactly three of any letter.
# You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

# import sys

# Text for console inputs
# inputs = [x[:-1]for x in sys.stdin.readlines()]

inputs = open("inputs.txt", "r").read().split("\n")
print(inputs)
counter2 = 0
counter3 = 0
for iD in inputs:
    occurencies = {}
    bool2Found = False
    bool3Found = False
    for char in iD:
        if char in occurencies.keys():
            occurencies[char] += 1
        else:
            occurencies[char] = 1
    for val in occurencies.values():
        if val == 2 and not bool2Found:
            counter2 += 1
            bool2Found = True
        elif val == 3 and not bool3Found:
            counter3 += 1
            bool3Found = True

print("checSum " + counter3 * counter2)
