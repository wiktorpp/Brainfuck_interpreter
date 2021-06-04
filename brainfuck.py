import sys
code = []
for opcode in open(sys.argv[1]).read():
    if opcode in [">", "<", "+", "-", ".", ",", "[", "]"]:
        code.append(opcode)
print("".join(code))
pointer = 0
memory = {0: 0}
inputBuffer = None
for opcode in code:
    if opcode == ">":
        pointer += 1
        memory[pointer] = 0
    elif opcode == "<":
        pointer -= 1
        memory[pointer] = 0
    elif opcode == "+":
        memory[pointer] += 1
    elif opcode == "-":
        memory[pointer] -= 1
    elif opcode == ".":
        print(chr(memory[pointer]), end="")
    elif opcode == ",":
        if inputBuffer == None:
            inputBuffer = [int(i) for i in input().encode()]
        memory[pointer] =  inputBuffer.pop(0)
print(memory)
