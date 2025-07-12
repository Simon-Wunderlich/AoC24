with open("4/input.txt") as f:
    inputStr = f.read()

inputArr = inputStr.split("\n")

total = 0

def isValid(txt):
    if txt == "MAS" or txt == "SAM":
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

def checkCross(lineNum, charNum):
    if lineNum - 1 < 0:
        return 0
    if charNum - 1 < 0:
        return 0
    try:
        line1 = ""
        line1 += inputArr[lineNum + 1][charNum -1]
        line1 += "A"
        line1 += inputArr[lineNum - 1][charNum +1]

        line2 = ""
        line2 += inputArr[lineNum - 1][charNum -1]
        line2 += "A"
        line2 += inputArr[lineNum + 1][charNum +1]
        if isValid(line1) and isValid(line2):
            return 1
    except:
        pass
    return 0


for lineNum in range(len(inputArr)):
    line = inputArr[lineNum]
    for charNum in range(len(line)):
        char = line[charNum]
        if char != "A":
            continue
        total += checkCross(lineNum, charNum)

print(total)