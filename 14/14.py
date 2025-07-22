import math
import re

X_BOUNDS = 101
Y_BOUNDS = 103
TIME_SPAN = 100

with open("input.txt") as f:
    guards = f.read().split("\n")

def parse(input):
    p = re.compile("-?\\d+")
    result =  p.findall(input)
    return [int(x) for x in result]

def calcPos(movement):
    x = (movement[0] + movement[2]*TIME_SPAN) % X_BOUNDS
    if x < 0:
        x += X_BOUNDS
    y = (movement[1] + movement[3]*TIME_SPAN) % Y_BOUNDS
    if y < 0:
        y += Y_BOUNDS

    return [x,y]

def getQuadrant(pos):
    if pos[0] == math.floor(X_BOUNDS / 2) or pos[1] == math.floor(Y_BOUNDS / 2):
        return -1
    
    if (pos[0] < math.floor(X_BOUNDS / 2)):
        quadrant = 0
    else:
        quadrant = 1

    if (pos[1] > math.floor(Y_BOUNDS / 2)):
            quadrant += 2

    return quadrant


quadrants = [0,0,0,0]

for guard in guards:
    movement = parse(guard)
    pos = calcPos(movement)
    quadrant = getQuadrant(pos)
    if quadrant != -1:
        quadrants[quadrant] += 1
    print(pos)

total = 1
for x in quadrants:
    total *= x
print(quadrants)
print(total)
