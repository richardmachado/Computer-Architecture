Bitwise operations
______________________________________

math ops that work 1 bit at a time in a number

A B A NAND B
______________
0  0   1
0  1   1
1  0   1
1  1   0

A  B   A & B (& is bitwise AND)
______________
0  0   0
0  1   0
1  0   0
1  1   1

A  B   A |  B (| is bitwise OR)
______________
0  0   0
0  1   1
1  0   1
1  1   1

A  B   A ^  B (^ is bitwise exclusive X88OR(and/or))
______________
0  0   0
0  1   1
1  0   1
1  1   0

A  ~A   (~ is bitwise NOT)
_____
0   1
1   0

F = 0 T = 1

In general

OR can be used to set bits to 1
AND can be used to clear bits to 0


______________________
Bit shifting
_______________________

  111001 >> shift right
  011100 << shift left
  001110
  000111
  000011
  000001
  000000

123456 >>
012345
001234
000123
000012
000001
000000

  123456 << 
 1234560 <<
12345600 <<

 vv 
12345 -> do some stuff and get ->23 
.MM..
02300 shift
00230 shift
00023 



