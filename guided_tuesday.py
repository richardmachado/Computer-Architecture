
import sys

memory = [] * 256

with open(sys.argv[1]) as f:
    for line in f:
        print(line, end="")
sys.exit()

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