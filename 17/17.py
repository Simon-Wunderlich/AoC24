import re
with open("17/input.txt") as f:
    inputStr = f.read()


def combo(val):
    if val <4:
        return val
    if val == 4:
        return A
    if val == 5:
        return B
    if val == 6:
        return C


#0
def adv(val):
    return int(A / pow(2,combo(val)))
#1
def bxl(val):
    return B ^ val

#2
def bst(val):
    return combo(val) % 8

#3
def jnz(val):
    global insPointer
    if A == 0:
        return insPointer
    insPointer = val;
    return val -2

#4
def bxc(val):
    return B ^ C

#5
def out(val):
    return str(combo(val) % 8)

#6
def bdv(val):
    return int(A / pow(2, combo(val)))

#7
def cdv(val):
    return int(A / pow(2, combo(val)))


insPointer = 0
tape = ""
def parse():
    global A
    global B
    global C
    global tape
    p = re.compile("\\d+\\n")
    result = p.findall(inputStr)
    A = int(result[0][0:-1])
    B = int(result[1][0:-1])
    C = int(result[2][0:-1])

    p = re.compile("(\\d+)(,|$)")
    result = p.findall(inputStr)
    for x in result:
        tape+= x[0]


def calc(_A):
    global A
    global B
    global C
    global insPointer
    output = ""
    A = int(_A,2)
    B = 0
    C = 0
    insPointer = 0
    while(insPointer < len(tape)):
        ins = tape[insPointer]
        if (ins == "0"):
            A = adv(int(tape[insPointer+1]))
        elif (ins == "1"):
            B = bxl(int(tape[insPointer+1]))
        elif (ins == "2"):
            B = bst(int(tape[insPointer+1]))
        elif (ins == "3"):
            insPointer = jnz(int(tape[insPointer+1]))
        elif (ins == "4"):
            B = bxc(int(tape[insPointer+1]))
        elif (ins == "5"):
            output += out(int(tape[insPointer+1]))
        elif (ins == "6"):
            B = bdv(int(tape[insPointer+1]))
        elif (ins == "7"):
            C = cdv(int(tape[insPointer+1]))
        insPointer+=2
    return output

def dfs(A_bin, index):
    if (index == len(tape)):
        return A_bin
    count = 0
    result = ""
    _A = A_bin
    while(count < 8):
        _A =  A_bin + format(count, f'03b')

        result = str(calc(_A))

        if len(result)>0:
            if result[0] == tape[-(index+1)]:
                result = dfs(_A, index+1)
                if result != "0":
                    return result
        count+=1
    return "0"
        
parse()
print(int(dfs("", 0),2))
