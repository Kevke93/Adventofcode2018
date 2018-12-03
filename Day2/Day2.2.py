# --- Part Two ---
# Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.
# The boxes will have IDs which differ by exactly one character at the same position in both strings. For example
# , given the following box IDs:
# abcde
# fghij
# klmno
# pqrst
# fguij
# axcye
# wvxyz
# The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij
# and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.
# What letters are common between the two correct box IDs?
# (In the example above, this is found by removing the differing character from either ID, producing fgij.)


import sys

# Text for console inputs
# inputs = [x[:-1]for x in sys.stdin.readlines()]

inputs = open("inputs.txt", "r").read().split("\n")

for i in range(len(inputs) - 2):
    for j in range(i + 1, len(inputs) - 1):
        checkFirst = inputs[i]
        checkSecond = inputs[j]

        differentChar = 0
        placeOfDifferentChar = None

        for k, char in enumerate(checkFirst):
            if char != checkSecond[k]:
                differentChar += 1
                placeOfDifferentChar = k
            if differentChar > 1:
                break

        if differentChar == 1:
            print(checkFirst[:placeOfDifferentChar] + checkFirst[placeOfDifferentChar + 1:])
            sys.exit()
