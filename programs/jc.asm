; tests the conditional jump instructions JC and JZ
; from "Conditional jump instructions", https://www.youtube.com/watch?v=Zg1NdPKoosU
0: OUT
1: ADD 15
2: JC 4
3: JMP 0
4: SUB 15
5: OUT
6: JZ 0
7: JMP 4
15: 64 ; make this 64 rather than 1 in original to speed up