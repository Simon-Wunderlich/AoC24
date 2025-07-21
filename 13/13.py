import re

class buttons():
    xA = 0
    xB = 0
    yA = 0
    yB = 0
    xT = 0
    yT = 0

with open("input.txt") as f:
    claws = f.read().split("\n\n")

def parseClaw(input):
    buttonArr = []
    p = re.compile("([+=])(.+?)(,|$)")
    for x in input.split("\n"):
        result = p.findall(x)
        buttonArr.append([result[0][1], result[1][1]])
    btns = buttons()
    btns.xA = int(buttonArr[0][0])
    btns.yA = int(buttonArr[0][1])
    btns.xB = int(buttonArr[1][0])
    btns.yB = int(buttonArr[1][1])
    btns.xT = int(buttonArr[2][0]) + 10000000000000
    btns.yT = int(buttonArr[2][1]) + 10000000000000
    return btns

currentButtons = buttons()

def calcPrice():
    xA = currentButtons.xA
    yA = currentButtons.yA
    xB = currentButtons.xB
    yB = currentButtons.yB
    xT = currentButtons.xT
    yT = currentButtons.yT

    b = (xA*yT - xT*yA) / (yB * xA - xB * yA)
    a = (xT - b * xB) / xA

    if  a < 0 and b < 0:
        return 0
    if (a+b) % 1 != 0:
        return 0
    return 3*a+b

total = 0
for x in claws:
    currentButtons = parseClaw(x)
    price = calcPrice()
    total+=price
print(total)