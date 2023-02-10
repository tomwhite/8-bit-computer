# Assemble a program for the 8-bit computer, suitable for loading
# into a CircuitJS1 SRAM component, representing the program memory.
#
# Each line has the following form:
#
# <address>: <opcode> <operand>
#
# or, to store data values:
#
# <address>: <value>
# 
# Anything after a semicolon ; is treated as a comment.
#

import sys

OPCODES = {
    "NOP": 0b0000,
    "LDA": 0b0001,
    "ADD": 0b0010,
    "SUB": 0b0011,
    "STA": 0b0100,
    "LDI": 0b0101,
    "JMP": 0b0110,
    "JC":  0b0111,
    "JZ":  0b1000,
    "OUT": 0b1110,
    "HLT": 0b1111,
}

input = sys.argv[1]

with open(input) as f:
    for line in f:
        if line.startswith(";"):
            continue
        line = line.split(";")[0]
        tokens = line.strip().split()
        address = int(tokens[0][:-1])
        op = tokens[1]
        if op not in OPCODES:
            code = int(op)  # treat as a data value
        else:
            low = int(tokens[2]) if len(tokens) == 3 else 0
            code = OPCODES[op] << 4 | low
        print(f"{address}: {code}")
