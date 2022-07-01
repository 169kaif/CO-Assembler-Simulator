assembly_instructions = []	

with open("CO_instructions.txt", "r") as f:
	for line in f:
		assembly_instructions.append(line)

d_registers = {'R0':'000', 'R1':'001', 'R2':'010', 'R3':'011', 'R4':'100', 'R5':'101', 'R6':'110', 'FLAGS':'111'}

correct_instructions = []
faulty_instructions = []

emptylines = 0

for instruction in assembly_instructions:
	if instruction == '\n':
		emptylines+=1

varlines=0

for instruction in assembly_instructions:
	if (instruction[0:3]=='var'):
		varlines += 1