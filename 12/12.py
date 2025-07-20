with open("input.txt") as f:
    landArr = f.read().split("\n")

totalCountedLand = []
sides = []
currentArea = 0
currentPerim = 0
totalPrice = 0

def calcLand(x,y):
    global currentArea
    global currentPerim
    global totalCountedLand
    global sides
    if (f"{x,y}" in totalCountedLand):
        return

    totalCountedLand.append(f"{x,y}")

    currentArea+=1
    if not checkLand(x + 1, y, landArr[y][x]):
        if (f"{x+0.5,float(y)}" not in sides):
            currentPerim+=1
            traverseSide(x+1,y,0, 1, -1,0, landArr[y][x])
            traverseSide(x+1,y,0, -1, -1,0, landArr[y][x])
    else:
        calcLand(x+1,y)


    if not checkLand(x - 1, y, landArr[y][x]):
        if (f"{x-0.5,float(y)}" not in sides):
            currentPerim+=1
            traverseSide(x-1,y,0, 1, 1,0, landArr[y][x])
            traverseSide(x-1,y,0, -1, 1,0, landArr[y][x])
    else:
        calcLand(x-1,y)


    if not checkLand(x, y+1, landArr[y][x]):
        if (f"{float(x),y+0.5}" not in sides):
            currentPerim+=1
            traverseSide(x,y+1,1, 0, 0,-1, landArr[y][x])
            traverseSide(x,y+1,-1, 0, 0,-1, landArr[y][x])
    else:
        calcLand(x,y+1)

    if not checkLand(x, y-1, landArr[y][x]):
        if (f"{float(x),y-0.5}" not in sides):
            currentPerim+=1
            traverseSide(x,y-1,1, 0, 0,1, landArr[y][x])
            traverseSide(x,y-1,-1, 0, 0,1,landArr[y][x])
    else:
        calcLand(x,y-1)



def checkLand(x,y, char):
    if not inBounds(x,y):
        return False
    if landArr[y][x] != char:
        return False
    return True

def inBounds(x,y):
    if x < 0:
        return False
    if x >= len(landArr[0]):
        return False
    if y < 0:
        return False
    if y >= len(landArr):
        return False
    return True

def traverseSide(x,y, dirx, diry, checkDirX, checkDirY, char):
    global currentArea
    global currentPerim
    global totalCountedLand
    global sides


    sides.append(f"{x+checkDirX/2,y+checkDirY/2}")

    if not inBounds(x,y):
        if (inBounds(x+checkDirX, y+checkDirY)):
            if char == landArr[y+checkDirY][x+checkDirX]:
                traverseSide(x+dirx,y+diry,dirx, diry, checkDirX, checkDirY, char)
        return

    if not inBounds(x+dirx,y+diry):
        return
    #
    # if not inBounds(x+checkDirX,y+checkDirY):
    #     return
    if landArr[y+diry][x+dirx] != char and landArr[y+checkDirY][x+checkDirX] == char:
        traverseSide(x+dirx,y+diry,dirx, diry, checkDirX, checkDirY, char)

for y, line in enumerate(landArr):
    for x, char in enumerate(line):
        currentPerim, currentArea = 0, 0
        sides = []
        calcLand(x,y)
        # print(f"{char}: {currentArea},{currentPerim}, ({' '.join(sides)})")
        totalPrice += currentArea * currentPerim
print(totalPrice)