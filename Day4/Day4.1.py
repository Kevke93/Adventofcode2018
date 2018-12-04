from datetime import datetime

inputs = open("inputs.txt", "r").read().split("\n")

splited = []

for string in inputs:
    dateTime = datetime.strptime(string[1:17], '%Y-%m-%d %H:%M')

    if string[19] == 'f':
        key = "0"
    elif string[19] == "w":
        key = "1"
    else:
        key = string.split()[3]
    splited.append([dateTime, key])
splited.sort()
sleep = {}
key = None
for i, line in enumerate(splited):
    if line[1][0] == '#':
        key = line[1][1:]
        if key not in sleep.keys():
            sleep[key] = [0] * 60
    elif line[1][0] == "1":
        for timesleep in range(line[0].minute - splited[i - 1][0].minute):
            sleep[key][splited[i - 1][0].minute + timesleep] += 1

worstGuard, frequenzySleeper, maxTimeAsleep, maxFrequenzy = None, None, 0, 0

for key, value in sleep.items():
    sumValue = sum(value)
    maxValue = max(value)
    if sumValue > maxTimeAsleep:
        maxTimeAsleep = sumValue
        worstGuard = key
    if maxFrequenzy < maxValue:
        maxFrequenzy = maxValue
        frequenzySleeper = key

bestMinuite, maxMin = None, 0

for i, minuite in enumerate(sleep[worstGuard]):
    if minuite > maxMin:
        maxMin = minuite
        bestMinuite = i

print("RESULT A1: " + str(int(worstGuard) * bestMinuite))
print("RESULT A2: " + str(int(frequenzySleeper) * sleep[frequenzySleeper].index(maxFrequenzy)))
