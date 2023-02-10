; output Fibonacci numbers
; from "Programming Fibonacci on a breadboard computer", https://www.youtube.com/watch?v=a73ZXDJtU48
0:  LDI 1   ; y=1
1:  STA 14  ; "
2:  LDI 0   ; x=0
3:  OUT
4:  ADD 14  ; z=x+y
5:  STA 15  ; "
6:  LDA 14  ; x=y
7:  STA 13  ; "
8:  LDA 15  ; y=z
9:  STA 14  ; "
10: LDA 13
11: JC 0    ; if result of ADD had carry bit then restart
12: JMP 3   ; otherwise loop
;13: x
;14: y
;15: z