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


d={"add":["A","10000"],"sub":["A","10001"],"mov":["B","10010"],"ld":["D","10100"],"st":["D","10101"],
  "mul":["A","10110"],"div":["C","10111"],"rs":["B","11000"],"ls":["B","11001"],"xor":["A","11010"],"or":["A","11011"],
  "and":["A","11100"],"not":["C","11101"],"cmp":["C","11110"],"jmp":["E","11111"],"jlt":["E","01100"],"jgt":["E","01101"],
  "je":["E","01111"],"hlt":["F","01010"]}#mov is in "c" and "b"		