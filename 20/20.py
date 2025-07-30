from collections import deque

with open("20/input.txt", 'r') as file:
    inputMap = [list(line.strip()) for line in file if line.strip()]

def bfs(x,y):
    global inputMap
    queue = deque()
    inputMap[y][x] = 0
    queue.append([x,y,0])

    while(queue):
        current = queue.popleft()
        x = current[0]
        y = current[1]
        score = current[2]

        steps = [
            (x+1,y),
            (x-1,y),
            (x,y+1),
            (x,y-1)
            ]

        for _x, _y in steps:
            if inputMap[_y][_x] == "#":
                continue

            if inputMap[_y][_x] in [".", "E"] or (isinstance(inputMap[_y][_x], int) and inputMap[_y][_x] > score+1):
                inputMap[_y][_x] = score+1
                queue.append([_x,_y,score+1])
    return inputMap

def scanForCheats(threshold):
    count = 0
    for y in range(1,len(inputMap)-1):
        for x in range(1,len(inputMap[y])-1):
            if (inputMap[y][x] == "#"):
                continue

            for _x in range(x + -20, x + 21):
                for _y in range(y + -20, y + 21):
                    if _x >= len(inputMap[0]) or _y >= len(inputMap) or _x < 0 or _y < 0:
                        continue
                    if isinstance(inputMap[_y][_x], int):
                        if inputMap[_y][_x] - inputMap[y][x] - abs(x-_x)-abs(y-_y) >= threshold and abs(x-_x)+abs(y-_y) <= 20:
                            count += 1
    return count

def genBfs():
    global inputMap
    for y in range(len(inputMap)):
        for x in range(len(inputMap[y])):
            if inputMap[y][x] == "S":
                return bfs(x,y)


genBfs()
print(scanForCheats(100))