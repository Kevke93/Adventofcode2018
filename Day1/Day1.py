#A1After feeling like you've been falling for a few minutes, you look at the device's tiny screen.
# "Error: Device must be calibrated before first use. Frequency drift detected. Cannot maintain destination lock."
# Below the message, the device shows a sequence of changes in frequency (your puzzle input).
# A value like +6 means the current frequency increases by 6; a value like -3 means the current
# frequency decreases by 3.
# A2
# You notice that the device repeats the same frequency change list over and over.
# To calibrate the device, you need to find the first frequency it reaches twice.

# import sys
# inputs =[int(x.replace("+","")) for x in sys.stdin.readlines()]

inputs = [int(x) for x in open("inputs.txt", "r").read().replace("+", "").split("\n")]

oldres = set()
oldres.add(0)
result = 0
notfound = True
task1 = False
while notfound:
    for x in inputs:
        result += x
        if result in oldres:
            print("repeated frequency " + str(result))
            notfound = False
            break
        else:
            oldres.add(result)

    if not task1:
        task1 = True
        print("Sum frequency " + str(result))