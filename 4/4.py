with open("4/input.txt") as f:
    inputStr = f.read()

inputArr = inputStr.split("\n")

total = 0

def isValid(txt):
    if txt == "XMAS" or txt == "SAMX":
        return True
    return False

def checkHor(lineNum, charNum, direction):
    if charNum + 3*direction< 0:
        return 0
    try:
        if isValid(inputArr[lineNum][min(charNum,charNum+3*direction):max(charNum+1,charNum+4*direction)]):
            return 1
    except:
        pass
    return 0

def checkVert(lineNum, charNum, direction):
    if lineNum + 3*direction< 0:
        return 0
    try:
        line = [x[charNum] for x in inputArr[min(lineNum,lineNum+3*direction):max(lineNum+1,lineNum+4*direction)]]
        if isValid("".join(line)):
            return 1
    except:
        pass
    return 0

def checkDiag(lineNum, charNum, xDir, yDir):
    if lineNum + 3*yDir < 0:
        return 0
    if charNum + 3*xDir < 0:
        return 0
    try:
        line = ""
        for x in range(4):
                line += inputArr[lineNum + x*yDir][charNum + x*xDir]
        if isValid("".join(line)):
            return 1
    except:
        pass
    return 0


for lineNum in range(len(inputArr)):
    line = inputArr[lineNum]
    for charNum in range(len(line)):
        char = line[charNum]
        if char != "X":
            continue
        total += checkHor(lineNum, charNum, 1)
        total += checkHor(lineNum, charNum, -1)
        total += checkVert(lineNum, charNum, 1)
        total += checkVert(lineNum, charNum, -1)
        total += checkDiag(lineNum, charNum, 1, 1)
        total += checkDiag(lineNum, charNum, 1, -1)
        total += checkDiag(lineNum, charNum, -1, 1)
        total += checkDiag(lineNum, charNum, -1, -1)

print(total)