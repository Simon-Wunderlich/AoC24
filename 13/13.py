import re
from functools import lru_cache


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
    p = re.compile("(\+|=)(.+?)(,|$)")
    for x in input.split("\n"):
        result = p.findall(x)
        buttonArr.append([result[0][1], result[1][1]])
    h = buttons()
    h.xA = int(buttonArr[0][0])
    h.yA = int(buttonArr[0][1])
    h.xB = int(buttonArr[1][0])
    h.yB = int(buttonArr[1][1])
    h.xT = int(buttonArr[2][0])
    h.yT = int(buttonArr[2][1])
    return h

currentButtons = buttons()


@lru_cache
def calcPrice(a,b, score):
    if [currentButtons.xT, currentButtons.yT] == findPos(a,b):
        return 3*a+b

    if findPos(a,b)[0] > currentButtons.xT and findPos(a,b)[1] > currentButtons.yT or a+b>200:
        return float('inf')

    temp1 = calcPrice(a+1, b, score)
    temp2 = calcPrice(a, b+1, score)

    return min(score, temp1, temp2)

def findPos(a,b):
    return [currentButtons.xA * a + currentButtons.xB * b, currentButtons.yA * a + currentButtons.yB * b]

total = 0
for x in claws:
    currentButtons = parseClaw(x)
    price = calcPrice(0,0,float('inf'))
    price = 0 if price == float('inf') else price
    total+=price
    print(price)
    calcPrice.cache_clear()
print(total)