with open("input.txt") as f:
    landArr = f.read().split("\n")

countedLand = []
currentArea = 0
currentPerim = 0
totalPrice = 0

def calcLand(x,y):
    global currentArea
    global currentPerim
    global countedLand
    if (f"{x,y}" in countedLand):
        return

    countedLand.append(f"{x,y}")

    currentArea+=1
    currentPerim = currentPerim + 1 if not checkLand(x + 1, y, landArr[y][x]) else currentPerim
    currentPerim = currentPerim + 1 if not checkLand(x - 1, y, landArr[y][x]) else currentPerim
    currentPerim = currentPerim + 1 if not checkLand(x, y + 1, landArr[y][x]) else currentPerim
    currentPerim = currentPerim + 1 if not checkLand(x, y - 1, landArr[y][x]) else currentPerim


def checkLand(x,y, char):
    if x < 0:
        return False
    if x >= len(landArr[0]):
        return False
    if y < 0:
        return False
    if y >= len(landArr):
        return False
    if landArr[y][x] != char:
        return False
    calcLand(x,y)
    return True

for y, line in enumerate(landArr):
    for x, char in enumerate(line):
        currentPerim, currentArea = 0, 0
        calcLand(x,y)
        totalPrice += currentArea * currentPerim
print(totalPrice)