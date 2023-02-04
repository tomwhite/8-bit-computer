# Build an 8-bit computer in CircuitJS1

This repo contains simulations and notes for Ben Eater's project to [build an 8-bit computer from scratch](https://eater.net/8bit).

Rather than build the project on breadboards, I created simulations of each module using [CircuitJS1](https://github.com/pfalstad/circuitjs1), an electronic circuit simulator that runs in the browser.

You can watch each video and try out the corresponding circuit to understand how the 8-bit computer works.

## 1. Clock module

[Astable 555 timer - 8-bit computer clock - part 1](https://www.youtube.com/watch?v=kRlSFm519Bo)

[Monostable 555 timer - 8-bit computer clock - part 2](https://www.youtube.com/watch?v=81BgFhm2vz8)

[Bistable 555 - 8-bit computer clock - part 3](https://www.youtube.com/watch?v=WCwJNnx36Rk)

[Clock logic - 8-bit computer clock - part 4](https://www.youtube.com/watch?v=SmQ5K7UQPMM)

## 2. Registers

[Bus architecture and how register transfers work - 8 bit register - Part 1](https://www.youtube.com/watch?v=QzWW-CBugZo)

[Tri-state logic: Connecting multiple outputs together - 8 bit register - Part 2](https://www.youtube.com/watch?v=faAjse109Q8)

| Video                                                                                                            | Circuit                           | Notes                                                         |
| ---------------------------------------------------------------------------------------------------------------- | --------------------------------- | ------------------------------------------------------------- |
| [Designing and building a 1-bit register - 8 bit register - Part 3](https://www.youtube.com/watch?v=-arYx_oVIj8) | _2.register-1-bit.circuitjs.txt_  | Built from logic gates, a D flip-flop, and a tri-state buffer |
| [Building an 8-bit register - 8-bit register - Part 4](https://www.youtube.com/watch?v=CiMaWbz_6E8)              | _2.register-custom.circuitjs.txt_ | Built using CircuitJS1's Custom Logic component               |
| [Testing our computer's registers - 8-bit register - Part 5](https://www.youtube.com/watch?v=9WE3Obdjtv0)        | _2.register-test.circuitjs.txt_   | Transfer the contents of one register to another              |

## 3. Arithmetic logic unit (ALU)

| Video                                                                                                          | Circuit               | Notes                                                                                     |
| -------------------------------------------------------------------------------------------------------------- | --------------------- | ----------------------------------------------------------------------------------------- |
| [Learn how computers add numbers and build a 4 bit adder circuit](https://www.youtube.com/watch?v=wvJc9CZcvBc) |                       | 1-bit adder is the Full Adder example in CircuitJS1, 4-bit adder is the Adder component   |
| [Twos complement: Negative numbers in binary](https://www.youtube.com/watch?v=4qH4unVtJkE)                     |                       | Theory                                                                                    |
| [ALU Design](https://www.youtube.com/watch?v=mOVOS9AjgFs)                                                      |                       |                                                                                           |
| [Building the ALU](https://www.youtube.com/watch?v=S-3fXU3FZQc)                                                | _3.alu.circuitjs.txt_ | Built using XOR gates, an 8-bit adder (rather than two 4-bit adders), and an 8-bit buffer |
| [Troubleshooting the ALU](https://www.youtube.com/watch?v=U7Q8-2YZTUU)                                         |                       | Debugging the wiring                                                                      |
| [Testing the computer's ALU](https://www.youtube.com/watch?v=4nCMDvnR2Fg)                                      | _3.alu.circuitjs.txt_ | Counting by twos                                                                          |

TODO: need to add CLR (clear) to registers

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

| Video                                                                 | Circuit | Notes                                                                                             |
| --------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------- |
| [Program counter design](https://www.youtube.com/watch?v=g_1HyxBzjl0) |         | In CircuitJS1 the 74LS161 4-bit binary counter is represented by the Counter with Load component. |
| [Program counter build](https://www.youtube.com/watch?v=tNwU7pK_3tk)  |         |                                                                                                   |

## 6. Output register

In CircuitJS1 we can cheat since there is a decimal display component, so there is no need to do any binary to decimal conversion. (However, it doesn't have the twos complement mode, and I couldn't see an easy way to do that. Since that is only used for display, we can do the conversion ourselves if needed.)

## 7. Bringing it all together

| Video                                                                                   | Circuit | Notes                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [8-bit computer build: Connecting the bus](https://www.youtube.com/watch?v=-6JAgFWCL9w) |         | Covers the output register, and uses a different chip. But I just used the same pattern as the other registers. Bus wiring is achieved in CircuitJS1 using labelled nodes. TODO: Do I need to pull bus to ground? |
| [8-bit CPU control signal overview](https://www.youtube.com/watch?v=AwUirxi9eBg)        |         | This is basically a wiring exercise. General note: I haven't needed to use LEDs in CircuitJS1, since you can see if a wire is high or low just by looking at it! (High is green, low is grey.)                    |

TODO: can we just make everything active high, so we don't need inverters?

Control lines:
| HLT MI | RI RO | IO II | AI AO | EO SU | BI OI | CE CO | J
