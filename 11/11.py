import math
from functools import cache

with open("input.txt") as f:
    stoneArr = f.read().split(" ")


@cache
def blink(stone, depth):
    global stoneCount
    if (depth == 76):
        return 1
    if stone == 0:
        stone = 1
        return blink(stone, depth + 1)

    orderMag = math.ceil(math.log(stone+0.1,10))
    if orderMag % 2 != 0:
        stone = stone*2024
        return blink(stone, depth + 1)
    else:
        cut = stone / math.pow(10, orderMag/2)

        left = math.floor(cut)

        right = round((cut - left)*math.pow(10, orderMag/2))

        return blink(right, depth + 1) + blink(left, depth + 1)

stoneCount = 0
for x in stoneArr:
    stoneCount += blink(int(x),1)
print(stoneCount)

