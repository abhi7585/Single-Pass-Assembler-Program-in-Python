"""
Instructions to the programmer:

1) Consider an hypothetical processor with approx. 20 assembly language instructions.
2) Define a standard MOT for the instructions with only 3 columns namely Mnemonics, Op-code & size. 
3) Write a sample ALP using few instructions from the MOT.
4) Do not used label addresses as it leads to forward reference problem which is not tackled in single pass assembler.
5) Write a program using any language to perform the assembly of the program.
6) Execute the program to generate the output of single pass assembly preferably in a tabular form.
7) The output shall display in 3 columns namely Relative address, ALP instruction & machine code.


Mnemonics	  		Op-code			Size
MOV R				01			1
ADD R				02			1
SUB R				03			1
MUL R				04			1
DIV R				05			1
AND R				06			1
OR R				07			1		
ADD data			08			2
SUB data			09			2
MUL data			10			2
DIV data			11			2
AND data			12			2
OR data				13			2
LOAD address    		14			3
STORE address   		15			3
DCR R				16			1
INC R				17			1
JMP address			18			3
JNZ address			19			3
HALT				20			1


Instruction with data is 2 byte, first byte is the op-code byte & second byte is data byte itself.
Instruction with address is 3 byte (as address assumed here is 16 bit), 
first byte is the op-code byte & second & third bytes are the address bytes.


Input assembly language program:

Consider very simple ALP with only 5 :-

ADD R 
SUB 30
STORE 1000 
HALT

Output after single pass assembly:-

Relative address			Instruction		Machine code
0					MOV R			01
1					ADD R			02
2					SUB 30			09, 30
4					STORE 1000		15, 10, 00
7					HALT			20

ASSUMPTIONS:
Let the Mnemonics of the instructions ADD R, SUB R, MUL R, DIV R, AND R, OR R be as A R, S R, M R, D R, AN R, O R. """


# PROGRAM:-

from sys import exit
motOpCode = {
    "MOV": 1,
    "A": 2,
    "S": 3,
    "M": 4,
    "D": 5,
    "AN": 6,
    "O": 7,
    "ADD": 8,
    "SUB": 9,
    "MUL": 10,
    "DIV": 11,
    "AND": 12,
    "OR": 13,
    "LOAD": 14,
    "STORE": 15,
    "DCR": 16,
    "INC": 17,
    "JMP": 18,
    "JNZ": 19,
    "HALT": 20
}

motSize = {
    "MOV": 1,
    "A": 1,
    "S": 1,
    "M": 1,
    "D": 1,
    "AN": 1,
    "O": 1,
    "ADD": 1,
    "SUB": 2,
    "MUL": 2,
    "DIV": 2,
    "AND": 2,
    "OR ": 2,
    "LOAD": 3,
    "STORE": 3,
    "DCR": 1,
    "INC": 1,
    "JMP": 3,
    "JNZ": 3,
    "HALT": 1
}

l = []
relativeAddress = []
machineCode = []
RA = 0
current = 0
count = 0
n = int(input("Enter the no of instruction lines : "))
for i in range(n):
    instructions = input("Enter instruction line {} : ".format(i + 1))
    l.append(instructions)
l = [x.upper() for x in l]		# Converting all the instructions to upper case
for i in range(n):
    x = l[i]
    if " " in x:
        s1 = ''.join(x)
        a, b = s1.split()
        if a in motOpCode:		# Checking if Mnemonics is present in MOT or not
            value = motOpCode.get(a)
            size = motSize.get(a)
            previous = size
            RA += current
            current = previous
            relativeAddress.append(RA)
            if b.isalpha() is True:
                machineCode.append(str(value))
            else:
                temp = list(b)
                for i in range(len(temp)):
                    if count == 2:
                        temp.insert(i, ',')
                        count = 0
                    else:
                        count = count + 1
                s = ''.join(temp)
                machineCode.append(str(value) + "," + s)
        else:
            print("Instruction is not in Op Code Table.")
            exit(0)				# EXIT if Mnemonics is not in MOT
    else:
        if x in motOpCode:
            value = motOpCode.get(x)
            size = motSize.get(x)
            previous = size
            RA += current
            current = previous
            relativeAddress.append(RA)
            machineCode.append(value)
        else:
            print("Instruction is not in Op Code Table.")
            exit(0)

print("Relative Address	Instruction	    OpCode")
for i in range(n):
    print(
        "{}                 {}          {}".format(relativeAddress[i], l[i], machineCode[i]))
