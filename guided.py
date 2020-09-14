
#! Number base
"""
It's the "language" that a number is written down in 

1100 = 12

Base 2: binary
Base 8: octal (rarely used)
Base 10: decimal (regular numners)
Base 16: hexadecimal (hex) - 0 - 9 and then a-f
Base 64: base 64

base 2 

0011 binary

1*2 1*1 = 3 decimal

binary digits ("bit")

8 bits == byte
4 bits == nybble

To specify base in code:

Prefix
___
none: decimal
0b    binary
0x    hex
0o    octal


yellow
#ffff00
red         green  blue
ff           ff   00        hex
255         255   0          decimal
11111111 11111111 0000000000 binary





0000 0 
0001 1
0010 2
0011 3
0100
0101
0110
0111


"""


memory = [
    1,
    3, #? save reg r1, 37
    1,
    37,
    4,
    1,
    2,

]

registers = [0] * 8

pc = 0 
running = True

while running:
    ir = memory[pc]


    if ir == 1:
        print("Richard")
        pc += 1

    elif ir == 2:
        running = False

    elif ir == 3:
        reg_num = memory[pc + 1]
        value = memory[pc+2 ]
        registers[reg_num] = value
        print(registers)
        pc +=3

    elif  ir ==4:
        reg_num = memory[pc+1]
        print(registers[reg_num])
        pc+=2
    else:
        print(f"Unknown instruction {b}")