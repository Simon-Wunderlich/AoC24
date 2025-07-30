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

def scanForCheats(threshold):
    count = 0
    for y in range(1,len(inputMap)-1):
        for x in range(1,len(inputMap[y])-1):
            if (inputMap[y][x] != "#"):
                continue

            checks = [
                ((x+1,y), (x-1,y)),
                ((x,y+1), (x,y-1))
                ]
            for p1, p2 in checks:
                if isinstance(inputMap[p1[1]][p1[0]], int) and isinstance(inputMap[p2[1]][p2[0]], int):
                    if abs(inputMap[p1[1]][p1[0]] - inputMap[p2[1]][p2[0]]) - 2 >= threshold:
                        count += 1
    return count


def genBfs():
    for y in range(len(inputMap)):
        for x in range(len(inputMap[y])):
            if inputMap[y][x] == "S":
                bfs(x,y)
                return
genBfs()
print(scanForCheats(100))