; multiplies two numbers
; from "Conditional jump instructions", https://www.youtube.com/watch?v=Zg1NdPKoosU
0: LDA 14
1: SUB 12
2: JC 6
3: LDA 13
4: OUT
5: HLT
6: STA 14
7: LDA 13
8: ADD 15
9: STA 13
10: JMP 0
12: 1
13: 0
14: 3 ; X
15: 5 ; Y