# Create a binary file for the 8-bit computer microcode, suitable for loading
# into a CircuitJS1 SRAM component, representing the EEPROMs.
#
# Based on https://github.com/beneater/eeprom-programmer/blob/master/microcode-eeprom-programmer/microcode-eeprom-programmer.ino

HLT = 0b1000000000000000  # Halt clock
MI =  0b0100000000000000  # Memory address register in
RI =  0b0010000000000000  # RAM data in
RO =  0b0001000000000000  # RAM data out
IO =  0b0000100000000000  # Instruction register out
II =  0b0000010000000000  # Instruction register in
AI =  0b0000001000000000  # A register in
AO =  0b0000000100000000  # A register out
EO =  0b0000000010000000  # ALU out
SU =  0b0000000001000000  # ALU subtract
BI =  0b0000000000100000  # B register in
OI =  0b0000000000010000  # Output register in
CE =  0b0000000000001000  # Program counter enable
CO =  0b0000000000000100  # Program counter out
J =   0b0000000000000010  # Jump (program counter in)

data = [
    MI|CO,  RO|II|CE,  0,      0,      0,         0, 0, 0,   # 0000 - NOP
    MI|CO,  RO|II|CE,  IO|MI,  RO|AI,  0,         0, 0, 0,   # 0001 - LDA
    MI|CO,  RO|II|CE,  IO|MI,  RO|BI,  EO|AI,     0, 0, 0,   # 0010 - ADD
    MI|CO,  RO|II|CE,  IO|MI,  RO|BI,  EO|AI|SU,  0, 0, 0,   # 0011 - SUB
    MI|CO,  RO|II|CE,  IO|MI,  AO|RI,  0,         0, 0, 0,   # 0100 - STA
    MI|CO,  RO|II|CE,  IO|AI,  0,      0,         0, 0, 0,   # 0101 - LDI
    MI|CO,  RO|II|CE,  IO|J,   0,      0,         0, 0, 0,   # 0110 - JMP
    MI|CO,  RO|II|CE,  0,      0,      0,         0, 0, 0,   # 0111
    MI|CO,  RO|II|CE,  0,      0,      0,         0, 0, 0,   # 1000
    MI|CO,  RO|II|CE,  0,      0,      0,         0, 0, 0,   # 1001
    MI|CO,  RO|II|CE,  0,      0,      0,         0, 0, 0,   # 1010
    MI|CO,  RO|II|CE,  0,      0,      0,         0, 0, 0,   # 1011
    MI|CO,  RO|II|CE,  0,      0,      0,         0, 0, 0,   # 1100
    MI|CO,  RO|II|CE,  0,      0,      0,         0, 0, 0,   # 1101
    MI|CO,  RO|II|CE,  AO|OI,  0,      0,         0, 0, 0,   # 1110 - OUT
    MI|CO,  RO|II|CE,  HLT,    0,      0,         0, 0, 0,   # 1111 - HLT
]

with open("roms/microcode.rom", "wb") as f:
    for address, value in enumerate(data):
        high = value >> 8
        f.write(bytes([high]))
    for address, value in enumerate(data):
        low = value & 0xFF
        f.write(bytes([low]))