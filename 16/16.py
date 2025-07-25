from collections import deque
with open("input.txt", 'r') as file:
    inputMap = [list(line.strip()) for line in file if line.strip()]


def leftTurn(dir):
    return [dir[1], -dir[0]]
def rightTurn(dir):
    return [-dir[1], dir[0]]

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

        allowedTurns = [
            (dir, score+1),
            (leftTurn(dir), score + 1001),
            (rightTurn(dir), score + 1001)
        ]

        for newDir, newScore in allowedTurns:
            if _map[y + newDir[1]][x + newDir[0]] == "#":
                continue

            if _map[y + newDir[1]][x + newDir[0]] in [".", "E"] or (isinstance(_map[y + newDir[1]][x + newDir[0]], int) and _map[y + newDir[1]][x + newDir[0]] > newScore):
                _map[y + newDir[1]][x + newDir[0]] = newScore
                queue.append([x+newDir[0], y+newDir[1], newDir, newScore])
    return _map[1][len(_map[1]) - 2]

print(bfs(inputMap))