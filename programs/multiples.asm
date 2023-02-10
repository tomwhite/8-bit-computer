; output multiples of 3
; from "Adding more machine language instructions to the CPU", https://www.youtube.com/watch?v=FCscQGBIL-Y
0: LDI  3
1: STA 15
2: LDI  0
3: ADD 15
4: OUT
5: JMP  3