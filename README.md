# Single-Pass-Assembler-Program-in-Python

Program of Single pass Assembler using Python programming language. This program is general specific for the mentioned cases in the program.
Instructions to the programmer:
1) Consider an hypothetical processor with approx. 20 assembly language instructions.
2) Define a standard MOT for the instructions with only 3 columns namely Mnemonics, Op-code & size. 
3) Write a sample ALP using few instructions from the MOT.
4) Do not used label addresses as it leads to forward reference problem which is not tackled in single pass assembler.
5) Write a program using any language to perform the assembly of the program.
6) Execute the program to generate the output of single pass assembly preferably in a tabular form.
7) The output shall display in 3 columns namely Relative address, ALP instruction & machine code.
```
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
```
Instruction with data is 2 byte, first byte is the op-code byte & second byte is data byte itself.
Instruction with address is 3 byte (as address assumed here is 16 bit), 
first byte is the op-code byte & second & third bytes are the address bytes.
Input assembly language program:

Consider very simple ALP with only 5 :-
```
MOV R
ADD R 
SUB 30
STORE 1000 
HALT
```
Output after single pass assembly:-
```
Relative address			Instruction		Machine code
0					MOV R			01
1					ADD R			02
2					SUB 30			09, 30
4					STORE 1000		15, 10, 00
7					HALT			20
```
ASSUMPTIONS:
Let the Mnemonics of the instructions ADD R, SUB R, MUL R, DIV R, AND R, OR R be as A R, S R, M R, D R, AN R, O R. """
