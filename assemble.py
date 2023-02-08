OPCODES = {
    "NOP": 0b0000,
    "LDA": 0b0001,
    "ADD": 0b0010,
    "SUB": 0b0011,
    "STA": 0b0100,
    "LDI": 0b0101,
    "JMP": 0b0110,
    "OUT": 0b1110,
    "HLT": 0b1111,
}
with open("times3.asm") as f:
    print("0: ", end="")
    for line in f:
        if line.startswith(";"):
            continue
        tokens = line.strip().split()
        op = tokens[0]
        low = int(tokens[1]) if len(tokens) == 2 else 0
        print(OPCODES[op] << 4 | low, end=" ")
    print()
