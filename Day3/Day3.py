# A1
# Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and
# consist of a single rectangle with edges parallel to the edges of the fabric.
#  Each claim's rectangle is defined as follows:
# The number of inches between the left edge of the fabric and the left edge of the rectangle.
# The number of inches between the top edge of the fabric and the top edge of the rectangle.
# The width of the rectangle in inches.
# The height of the rectangle in inches.

# A2
# Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square
# inch of fabric with any other claim.
# If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

import re

inputs = open("inputs.txt", "r").read().split("\n")
space = {}

for line in inputs:
    split = re.split(' @ |,|: |x', line)
    ID, startLeft, startTop, rectWidth, rectHeidht = split[0], int(split[1]) + 1, int(split[2]) + 1, \
                                                     int(split[3]), int(split[4])

    for i in range(startLeft, startLeft + rectWidth):
        for j in range(startTop, startTop + rectHeidht):

            if str(i) + ":" + str(j) in space.keys():
                space[str(i) + ":" + str(j)] += 1

            else:
                space[str(i) + ":" + str(j)] = 1
overlap = 0
for value in space.values():
    if value >= 2:
        overlap += 1

print("There is a overlapping Space of " + str(overlap))

# same as before put this time check if the all the spaces are equal to one

for line in inputs:
    split = re.split(' @ |,|: |x', line)
    ID, startLeft, startTop, rectWidth, rectHeidht = split[0], int(split[1]) + 1, int(split[2]) + 1, \
                                                     int(split[3]), int(split[4])
    foundSantas = True

    for i in range(startLeft, startLeft + rectWidth):
        for j in range(startTop, startTop + rectHeidht):
            if space[str(i) + ":" + str(j)] != 1:
                foundSantas = False
                break
    if foundSantas:
        print("Santas Stuff has been found: " + str(ID))
        break

