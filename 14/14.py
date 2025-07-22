import re
from functools import cache

X_BOUNDS = 101
Y_BOUNDS = 103

with open("input.txt") as f:
    guards = f.read().split("\n")
@cache
def parse(input):
    p = re.compile("-?\\d+")
    result =  p.findall(input)
    return [int(x) for x in result]

def calcPos(movement, _timeSpan):
    x = (movement[0] + movement[2] * _timeSpan) % X_BOUNDS
    if x < 0:
        x += X_BOUNDS
    y = (movement[1] + movement[3] * _timeSpan) % Y_BOUNDS
    if y < 0:
        y += Y_BOUNDS

    return [x,y]

# FIND TIME TO LOOP BACK TO START POSITIONS
# RESULT: 10403 seconds
# initPos = []
# currentPoses = []
# prevPosList = []
# iterations = 0
# for guard in guards:
#     movement = parse(guard)
#     initPos.append([movement[0], movement[1]])
# prevPosList = initPos
#
# while True:
#     for x, guard in enumerate(guards):
#         movement = parse(guard)
#         movement[0] = prevPosList[x][0]
#         movement[1] = prevPosList[x][1]
#         pos = calcPos(movement,1)
#         currentPoses.append(pos)
#     iterations+=1
#     if currentPoses == initPos:
#         print(iterations)
#         break
#     prevPosList = currentPoses
#     currentPoses = []

def calcDists(posList):
    totalDist = 0
    for i in posList:
        for j in posList:
            totalDist += abs(i[0]-j[0]) + abs(i[1] - j[1])
    return totalDist


positions = []
minDist = float('inf')
minDistTime = 0
for t in range (10403):
    for guard in guards:
        mov = parse(guard)
        positions.append(calcPos(mov, t))
    dist = calcDists(positions)
    if dist < minDist:
        minDist = dist
        minDistTime = t
    positions = []

print(minDistTime)