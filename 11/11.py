with open("11/input.txt") as f:
    stoneArr = f.read().split(" ")
def blink(stones):
    i = 0
    while i < len(stones):
        if stones[i] == "0":
            stones[i] = "1"
            i+=1
            continue
        if len(stones[i]) % 2 != 0:
            stones[i] = str(int(stones[i])*2024)
            i+=1
            continue
        else:
            rightHalf = str(int(stones[i][int(len(stones[i])/2):]))
            leftHalf = str(int(stones[i][:int(len(stones[i])/2)]))
            stones.pop(i)
            stones.insert(i, rightHalf)
            stones.insert(i, leftHalf)
            i+=2

    return stones

for x in range(25):
    stoneArr = blink(stoneArr)
print(len(stoneArr))
