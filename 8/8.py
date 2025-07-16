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
    for pos1 in positions[char]:
        for pos2 in positions[char]:
            if pos1 == pos2:
                continue
            antiNodeLocation = antiNodePos(pos2, pos1)
            if antiNodeLocation in antiNodesPos:
                continue
            if antiNodeLocation[0] >= len(inputArr[0]) or antiNodeLocation[0] < 0:
                continue
            if antiNodeLocation[1] >= len(inputArr) or antiNodeLocation[1] < 0:
                continue
            antiNodesPos.append(antiNodeLocation)

print(len(antiNodesPos))

