import re
with open("17/input.txt") as f:
    inputStr = f.read()

A, B, C = 0,0,0

insPointer = 0
tape = ""


def combo(val):
    if val <4:
        return val
    if val == 4:
        return A
    if val == 5:
        return B
    if val == 6:
        return C

def adv(val):
    global A
    A /= pow(2,combo(val))
    A = int(A)

def bxl(val):
    global B
    B ^= val

def bst(val):
    global B
    B = combo(val) % 8

def jnz(val):
    global A
    global insPointer
    if A == 0:
        return False
    insPointer = val;
    return True

def bxc(val):
    global B
    B = B ^ C

def out(val):
    global output
    output += str(combo(val) % 8)

def bdv(val):
    global B
    B = int(A / pow(2, combo(val)))

def cdv(val):
    global C
    C = int(A / pow(2, combo(val)))


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


parse()
output = ""
while(insPointer < len(tape)):
    ins = tape[insPointer]
    if (ins == "0"):
        adv(int(tape[insPointer+1]))
    if (ins == "1"):
        bxl(int(tape[insPointer+1]))
    if (ins == "2"):
        bst(int(tape[insPointer+1]))
    if (ins == "3"):
        if jnz(int(tape[insPointer+1])):
            insPointer -= 2
    if (ins == "4"):
        bxc(int(tape[insPointer+1]))
    if (ins == "5"):
        out(int(tape[insPointer+1]))
    if (ins == "6"):
        bdv(int(tape[insPointer+1]))
    if (ins == "7"):
        cdv(int(tape[insPointer+1]))
    insPointer+=2

print(",".join(output))