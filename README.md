# Build an 8-bit computer in CircuitJS1

This repo contains simulations and notes for Ben Eater's project to [build an 8-bit computer from scratch](https://eater.net/8bit).

Rather than build the project on breadboards, I created simulations of each module using [CircuitJS1](https://github.com/pfalstad/circuitjs1), an electronic circuit simulator that runs in the browser.

You can watch each video and try out the corresponding circuit to understand how the 8-bit computer works.

All the videos are on [YouTube](https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE405J2565dvjafglHU).

## 1. Clock module

| Video                                                                                               | Circuit                 | Notes |
| --------------------------------------------------------------------------------------------------- | ----------------------- | ----- |
| [Astable 555 timer - 8-bit computer clock - part 1](https://www.youtube.com/watch?v=kRlSFm519Bo)    |                         |       |
| [Monostable 555 timer - 8-bit computer clock - part 2](https://www.youtube.com/watch?v=81BgFhm2vz8) |                         |       |
| [Bistable 555 - 8-bit computer clock - part 3](https://www.youtube.com/watch?v=WCwJNnx36Rk)         |                         |       |
| [Clock logic - 8-bit computer clock - part 4](https://www.youtube.com/watch?v=SmQ5K7UQPMM)          | _1.clock.circuitjs.txt_ |       |

## 2. Registers

| Video                                                                                                                          | Circuit                           | Notes                                                         |
| ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- | ------------------------------------------------------------- |
| [Bus architecture and how register transfers work - 8 bit register - Part 1](https://www.youtube.com/watch?v=QzWW-CBugZo)      |                                   |                                                               |
| [Tri-state logic: Connecting multiple outputs together - 8 bit register - Part 2](https://www.youtube.com/watch?v=faAjse109Q8) |                                   |                                                               |
| [Designing and building a 1-bit register - 8 bit register - Part 3](https://www.youtube.com/watch?v=-arYx_oVIj8)               | _2.register-1-bit.circuitjs.txt_  | Built from logic gates, a D flip-flop, and a tri-state buffer |
| [Building an 8-bit register - 8-bit register - Part 4](https://www.youtube.com/watch?v=CiMaWbz_6E8)                            | _2.register-custom.circuitjs.txt_ | Built using CircuitJS1's Custom Logic component               |
| [Testing our computer's registers - 8-bit register - Part 5](https://www.youtube.com/watch?v=9WE3Obdjtv0)                      | _2.register-test.circuitjs.txt_   | Transfer the contents of one register to another              |

## 3. Arithmetic logic unit (ALU)

| Video                                                                                                          | Circuit               | Notes                                                                                     |
| -------------------------------------------------------------------------------------------------------------- | --------------------- | ----------------------------------------------------------------------------------------- |
| [Learn how computers add numbers and build a 4 bit adder circuit](https://www.youtube.com/watch?v=wvJc9CZcvBc) |                       | 1-bit adder is the Full Adder example in CircuitJS1, 4-bit adder is the Adder component   |
| [Twos complement: Negative numbers in binary](https://www.youtube.com/watch?v=4qH4unVtJkE)                     |                       | Theory                                                                                    |
| [ALU Design](https://www.youtube.com/watch?v=mOVOS9AjgFs)                                                      |                       |                                                                                           |
| [Building the ALU](https://www.youtube.com/watch?v=S-3fXU3FZQc)                                                | _3.alu.circuitjs.txt_ | Built using XOR gates, an 8-bit adder (rather than two 4-bit adders), and an 8-bit buffer |
| [Troubleshooting the ALU](https://www.youtube.com/watch?v=U7Q8-2YZTUU)                                         |                       | Debugging the wiring                                                                      |
| [Testing the computer's ALU](https://www.youtube.com/watch?v=4nCMDvnR2Fg)                                      | _3.alu.circuitjs.txt_ | Counting by twos                                                                          |

## 4. Random access memory (RAM) module

| Video                                                                                 | Circuit                   | Notes                                                                                                                                                                             |
| ------------------------------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [8-bit computer RAM intro](https://www.youtube.com/watch?v=FnxPIZR1ybs)               |                           | Theory                                                                                                                                                                            |
| [RAM module build - part 1](https://www.youtube.com/watch?v=uYXwCBo40iA)              | _4.ram.circuitjs.txt_     | CircuitJS1 has a SRAM component. However it doesn't have separate input and output pins unlike the chip used in the video, so we need another tri-state buffer on the write side. |
| [RAM module build - part 2](https://www.youtube.com/watch?v=KNve2LCcSRc)              | _4.ram-mar.circuitjs.txt_ | Memory Address Register                                                                                                                                                           |
| [RAM module build - part 3](https://www.youtube.com/watch?v=5rl1tEFXKt0)              |                           | Data lines. I didn't add the DIP switches for the data lines, since CircuitJS1 allows you to edit the contents of the SRAM directly.                                              |
| [RAM module testing and troubleshooting](https://www.youtube.com/watch?v=Vw3uDOUJRGw) |                           | A bit of debugging, then tests. Also labels control wires. I didn't implement the leading edge detector with a resistor and capacitor (should not affect correctness).            |

I struggled to get the RAM working. I noticed a lot of high current flows, which is a sign something is wrong. The mistake was that I was using an 8-bit register (custom logic) on the input side to the RAM. This was a problem because it is clocked, and a part of the logic sets the output to the input when there is no change. I think this was conflicting with the output of the RAM component, which also sets the same pins. When I changed the 8-bit register to an 8-bit buffer (which has no CLK), it worked.

## 5. Program counter

| Video                                                                 | Circuit              | Notes                                                                                             |
| --------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------- |
| [Program counter design](https://www.youtube.com/watch?v=g_1HyxBzjl0) |                      | In CircuitJS1 the 74LS161 4-bit binary counter is represented by the Counter with Load component. |
| [Program counter build](https://www.youtube.com/watch?v=tNwU7pK_3tk)  | _5.pc.circuitjs.txt_ |                                                                                                   |

## 6. Output register

In CircuitJS1 we can cheat since there is a decimal display component, so there is no need to do any binary to decimal conversion. (However, it doesn't have the twos complement mode, and I couldn't see an easy way to do that. Since that is only used for display, we can do the conversion ourselves if needed.)

See _6.output.circuitjs.txt_

## 7. Bringing it all together

| Video                                                                                   | Circuit | Notes                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [8-bit computer build: Connecting the bus](https://www.youtube.com/watch?v=-6JAgFWCL9w) |         | Covers the output register, and uses a different chip. But I just used the same pattern as the other registers. Bus wiring is achieved in CircuitJS1 using labelled nodes.                     |
| [8-bit CPU control signal overview](https://www.youtube.com/watch?v=AwUirxi9eBg)        |         | This is basically a wiring exercise. General note: I haven't needed to use LEDs in CircuitJS1, since you can see if a wire is high or low just by looking at it! (High is green, low is grey.) |

Control lines:
| HLT MI | RI RO | IO II | AI AO | EO SU | BI OI | CE CO | J

## 8. CPU control logic

[8-bit CPU control logic: Part 1](https://www.youtube.com/watch?v=dXdoim96v5A)

We get to define the opcodes! As long as we can express on the computer we can do what we like.

Here is the first program:

```
[1] [2]  [3]  [4]  [5]
LDA  14 0000 0001|1110 ; load contents of memory address 14 into the A register
ADD  15 0001 0010|1111 ; add the contents of memory address 14 to the A register
OUT     0010 1110|0000 ; move the contents of the A register to the output register
        1110 0001|1100 ; value 28
        1111 0000|1110 ; value 14
```

- `[1]` is the operator/opcode
- `[2]` is the operand
- `[3]` is the address in RAM
- `[4]` is the 4 bit number for the operator
- `[5]` is the 4 bit number for the operand

In the notation that CircuitJS1 uses for the contents of a SRAM chip, this is

```
0: 30 47 224
14: 28 14
```

So rather than programming the computer with DIP switches, we can just edit the memory directly, which is a lot easier.

Each instruction is broken into multiple micro instructions, as follows. These can be manually executed on the computer.

```
LDA 14
------
CO MI ; move PC to memory address register
RO II ; move memory contents to instruction register
CE    ; increment PC

IO MI ; move instruction register address (lower 4 bits) to memory address register
RO AI ; move memory contents to A register

ADD 15
------
CO MI ; move PC to memory address register
RO II ; move memory contents to instruction register
CE    ; increment PC

IO MI ; move instruction register address (lower 4 bits) to memory address register
RO BI ; move memory contents to B register
EO AI ; move sum from ALU to A register

OUT
---
CO MI
RO II
CE

AO OI ; move A register to output register
```

First 3 steps for each command are to fetch the instruction and increment the program counter.

Saved in _8.control1.circuitjs.txt_

[8-bit CPU control logic: Part 2](https://www.youtube.com/watch?v=X7rCxs1ppyY)

Started to build the logic. Used a regular counter (don't need one with load), and a demultiplexer.

[8-bit CPU control logic: Part 3](https://www.youtube.com/watch?v=dHWFpkGsxOs)

```
Instruction  Step HLT MI RI RO IO II AI AO  EO SU BI OI CE CO J

XXXX         000      1                                    1
XXXX         001            1     1                     1

0001         010      1        1
0001         011            1        1
0001         100

0010         010      1        1
0010         011            1                     1
0010         100                     1         1

1110         010                        1            1
1110         011
1110         100
```

Wrote a little python program _create_mem.py_ to convert to CircuitJS1 notation. This is equivalent to the EEPROM programming from the video.

[8-bit CPU reset circuit and power supply tips](https://www.youtube.com/watch?v=HtFro0UKqkk)

Reset (CLR)

[Reprogramming CPU microcode with an Arduino](https://www.youtube.com/watch?v=JUVt_KYAp-I)

Run `python microcode.py` and then `hexdump -Cv microcode.rom` to look at it (it should match the video).

Then upload to both "EEPROM" chips in CircuitJS1. Also change pin A on the right hand EEPROM to 1.

Compute 5 + 6 - 7 (=4)

```
LDA  15 0000 0001|1111
ADD  14 0001 0010|1110
SUB  13 0010 0011|1101
OUT     0011 1110|0000
HLT     0100 1111|0000
        1101 0000|0111
        1110 0000|0110
        1111 0000|0101
```

In CircuitJS1 notation:

```
0: 31 46 61 224 240
13: 7 6 5
```

[Adding more machine language instructions to the CPU](https://www.youtube.com/watch?v=FCscQGBIL-Y)

Output multiples of 3. (Note, no data in this program, since we use LDI, load immediate.)

```
LDI  3 0000 0101|0011
STA 15 0001 0100|1111
LDI  0 0010 0101|0000
ADD 15 0011 0010|1111
OUT    0100 1110|0000
JMP  3 0101 0110|0011
```

```
0: 83 79 80 47 224 99
```

Saved in _8.control3.circuitjs.txt_

[Making a computer Turing complete](https://www.youtube.com/watch?v=AqNDk_UJW4k)

Theory

[CPU flags register](https://www.youtube.com/watch?v=ObnosznZvHY)

CircuitJS1 has an 8-bit NOR gate we can use

[Conditional jump instructions](https://www.youtube.com/watch?v=Zg1NdPKoosU)

[Programming Fibonacci on a breadboard computer](https://www.youtube.com/watch?v=a73ZXDJtU48)
