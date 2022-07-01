assembly_instructions = []	

with open("CO_instructions.txt", "r") as f:
	for line in f:
		assembly_instructions.append(line)

correct_instructions = []
faulty_instructions = []

emptylines = 0
emptyline_index = []

for (index,instruction) in enumerate(assembly_instructions):
	if instruction == '\n':
		emptyline_index.append(index)
		emptylines+=1

varlines = 0
var_index = []

for (index,instruction) in enumerate(assembly_instructions):
	if (instruction[0:3]=='var'):
		var_index.append(index)
		varlines += 1

d_registers = {'R0':'000', 'R1':'001', 'R2':'010', 'R3':'011', 'R4':'100', 'R5':'101', 'R6':'110', 'FLAGS':'111'}

d={"add":["A","10000"],"sub":["A","10001"],"mov":["B","10010"],"ld":["D","10100"],"st":["D","10101"],
  "mul":["A","10110"],"div":["C","10111"],"rs":["B","11000"],"ls":["B","11001"],"xor":["A","11010"],"or":["A","11011"],
  "and":["A","11100"],"not":["C","11101"],"cmp":["C","11110"],"jmp":["E","11111"],"jlt":["E","01100"],"jgt":["E","01101"],
  "je":["E","01111"],"hlt":["F","01010"]}#mov is in "c" and "b"		

def f_A(a):
	reg1 = d_registers[a[1]]
	reg2 = d_registers[a[2]]
	reg3 = d_registers[a[3]]

	print('00' + reg1 + reg2 + reg3)

  #testcommit pavit

  #variable assignment function to be inserted here

  #label check niggers

for (index,line) in assembly_instructions:
	a = line.split()
	if index in emptyline_index:
		continue
	if index in var_index:
		continue

	if a[0] in d.keys():
		if d[a[0]][0] == 'A':
			print(d[a[0]][1], end='')
			f_A(a)       