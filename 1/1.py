with open("1/input.txt") as f:
    inputStr = f.read()

def sort(array, index):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i][index] > array[j][index]:
                array[i][index], array[j][index] = array[j][index], array[i][index]


inputList = inputStr.split('\n')
nestedInputList = [x.split("   ") for x in inputList]

sort(nestedInputList, 0)
sort(nestedInputList, 1)

print("Ordered lists")
print("\n".join(["   ".join(x) for x in nestedInputList]))

print("\nTotal distance")
output = [abs(int(x[1]) - int(x[0])) for x in nestedInputList]
print(sum(output))