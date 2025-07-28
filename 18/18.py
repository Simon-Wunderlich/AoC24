from collections import deque

X_BOUNDS = 70
Y_BOUNDS = 70
START_NUM_BYTES = 1024
with open("18/input.txt") as f:
    completebyteList = f.read().split()

def bfs(byteList):
    queue = deque()
    queue.append([0 ,0,0])
    points = {f"{X_BOUNDS},{Y_BOUNDS}":float('inf')}
    while(queue):
        current = queue.popleft()
        x = current[0]
        y = current[1]
        steps = current[2]

        potentialSteps = [
            (x+1,y),
            (x-1,y),
            (x,y+1),
            (x,y-1)
            ]

        for _x,_y in potentialSteps:
            if f"{_x},{_y}" in byteList or _x > X_BOUNDS or _x < 0 or _y > Y_BOUNDS or _y < 0:
                continue
            if f"{_x},{_y}" not in points or (f"{_x},{_y}" in points and points[f"{_x},{_y}"] > steps+1):
                if f"{_x},{_y}" not in points:
                    points.update({f"{_x},{_y}" : steps+1})
                else:
                    points[f"{_x},{_y}"] = steps+1
                queue.append([_x,_y,steps+1])

    return points[f"{X_BOUNDS},{Y_BOUNDS}"]


low = START_NUM_BYTES
high = len(completebyteList)-1
while high > low+1:
    index = int((low + high)/2)
    steps = bfs(completebyteList[0:index])
    if steps != float('inf'):
        low = index
    else:
        high = index
print(completebyteList[index-1])