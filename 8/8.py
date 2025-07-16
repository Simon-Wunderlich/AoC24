import numpy as np

def antiNodePos(pointA, pointB):
    vectorA = np.array(pointA)
    vectorB = np.array(pointB)
    return (2*vectorB- vectorA).tolist();


#key: antenna char
#value: array of all coords
positions = {} 
#list of all antinode coords
antiNodesPos = []

with open("8/input.txt") as f:
    inputStr = f.read()

inputArr = inputStr.split("\n")

for y, line in enumerate(inputArr):
    for x, char in enumerate(line):
        if char == ".":
            continue
        if char in positions:
            positions[char].append([x,y])
        else:
            positions.update({char : [[x,y]]})

for char in positions:
    for posA in positions[char]:
        for posB in positions[char]:
            pos1 = posA
            pos2 = posB

            if pos1 == pos2:
                continue

            if pos1 not in antiNodesPos:
                    antiNodesPos.append(pos1)

            if pos2 not in antiNodesPos:
                    antiNodesPos.append(pos2)

            inBounds = True
            while inBounds:
                antiNodeLocation = antiNodePos(pos2, pos1)
                if antiNodeLocation in antiNodesPos:
                    pos2 = pos1
                    pos1 = antiNodeLocation
                    continue
                if antiNodeLocation[0] >= len(inputArr[0]) or antiNodeLocation[0] < 0:
                    inBounds = False
                    continue
                if antiNodeLocation[1] >= len(inputArr) or antiNodeLocation[1] < 0:
                    inBounds = False
                    continue
                antiNodesPos.append(antiNodeLocation)
                pos2 = pos1
                pos1 = antiNodeLocation

print(len(antiNodesPos))