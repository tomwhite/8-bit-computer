LDI 0x1   ; y=1
STA [0xe] ; "
LDI 0x0   ; x=0
OUT
ADD [0xe] ; z=x+y
STA [0xf] ; "
LDA [0xe] ; x=y
STA [oxd] ; "
LDA [0xf] ; y=z
STA [0xe] ; "
LDA [0xd]
JC 0x0    ; if result of ADD had carry bit then restart
JMP 0x3   ; otherwise loop