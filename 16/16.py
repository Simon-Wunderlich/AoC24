from collections import deque
with open("input.txt", 'r') as file:
    inputMap = [list(line.strip()) for line in file if line.strip()]


def leftTurn(dir):
    return [dir[1], -dir[0]]
def rightTurn(dir):
    return [-dir[1], dir[0]]

def sign(x):
    return x / abs(x)

def bfs(_map):
    queue = deque()
    start = [1, len(_map) - 2, [1, 0], 0]
    _map[len(_map) - 2][1] = 0
    queue.append(start)

    while queue:
        current = queue.popleft()
        x = current[0]
        y = current[1]
        dir = current[2]
        score = current[3]
        if isinstance(_map[y][x], int):
            if _map[y][x] < score:
                continue

        allowedTurns = [
            (dir, score),
            (leftTurn(dir), score + 1000),
            (rightTurn(dir), score + 1000)
        ]
        children = []
        for newDir, newScore in allowedTurns:
            if _map[y + newDir[1]][x + newDir[0]] == "#":
                continue

            if _map[y + newDir[1]][x + newDir[0]] in [".", "E"] or (isinstance(_map[y + newDir[1]][x + newDir[0]], int) and (_map[y + newDir[1]][x + newDir[0]] > newScore)):
                # _map[y + newDir[1]][x + newDir[0]] = newScore + 1
                children.append(newScore)
                queue.append([x+newDir[0], y+newDir[1], newDir, newScore+1])
        if len(children) > 0:
            _map[y][x] = min(children)
        if (y == 1 and x == len(_map[0])-2):
            _map[y][x] =score
    return _map

points = [[len(inputMap[0])-2, 1]]
def dfs(_map, x,y):
    global points
    currentScore = _map[y][x]
    pointList = [
        ([x+1,y], _map[y][x+1]),
        ([x-1,y], _map[y][x-1]),
        ([x,y+1], _map[y+1][x]),
        ([x,y-1], _map[y-1][x])
    ]
    for point, score in pointList:
        if isinstance(score, int):
            if (score - currentScore <= 0 and score - currentScore > -2) or (score - currentScore <= -995 and score - currentScore > -1005) and point not in points:
                points.append(point)
                dfs(_map, point[0], point[1])
emptyMap = []

for line in inputMap:
    newLine = []
    for char in line:
        newLine.append(char)
    emptyMap.append(newLine)
filledMap = bfs(inputMap)

dfs(filledMap, len(filledMap[0])-2, 1)
for x in range(len(emptyMap)):
    for i in range(len(emptyMap[x])):
        if [i,x] in points:
            emptyMap[x][i] = "\033[94mO\033[0m"

for line in emptyMap:
    lineStr = ""
    for char in line:
        lineStr+= str(char)
    print(lineStr)
print(len(points))