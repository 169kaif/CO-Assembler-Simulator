# CO--SimpleAssembler and SimpleSimulator
Created a Simple Assembler and Simple Simulator as a project for the course CSE112 (CO - Computer Organisation).

## What the project contains?
The project contains an assembler, a simulator, a pdf document containing the ISA and the remaining questions.

## Functioning of the assembler
The assembler receives as input a text file containing valid syntax which is converted into binary using the ISA as reference and an output text file is generated.

## Functioning of the simulator
The simulator also recieves as input a text file containing binary. The binary instructions are then loaded into system memory by the simulator and the code is executed
starting at address 0 and continues until halt is reached.
After the execution of each instruction, the simulator outputs a single line containing an 8 bit number denoting the program counter. 
This is followed by 8 space separated 16 bit binary numbers denoting the values of the registers (R0, R1, ... R6 and FLAGS).

The output is as follows:
`<PC (8 bits)><space><R0 (16 bits)><space>...<R6 (16 bits)><space><FLAGS (16 bits)>`
  
## Using the project
Simply clone the project locally and run the python scripts
