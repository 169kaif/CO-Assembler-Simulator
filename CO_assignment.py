assembly_instructions = []	

with open("CO_instructions.txt", "r") as f:
	for line in f:
		if line=="\n":
			continue
		else:
			assembly_instructions.append(line)
correct_instructions = []
faulty_instructions = []



varlines = 0
var_index = []
ind=0
while assembly_instructions[ind][0:3]=="var":
	var_index.append(ind)
	ind+=1
	varlines+=1

#variable bakchodi

var_val = len(assembly_instructions) - varlines

d_var = {}

for index,line in enumerate(assembly_instructions):
	ls = line.split()
	if ls[0]=='var' and index in var_index:
		if ls[1] not in d_var.keys():
			d_var[ls[1]] = format(var_val, '08b')
			var_val+=1


d_registers = {'R0':'000', 'R1':'001', 'R2':'010', 'R3':'011', 'R4':'100', 'R5':'101', 'R6':'110', 'FLAGS':'111'}

d={"add":["A","10000"],"sub":["A","10001"],"mov":["B","10010"],"ld":["D","10100"],"st":["D","10101"],
  "mul":["A","10110"],"div":["C","10111"],"rs":["B","11000"],"ls":["B","11001"],"xor":["A","11010"],"or":["A","11011"],
  "and":["A","11100"],"not":["C","11101"],"cmp":["C","11110"],"jmp":["E","11111"],"jlt":["E","01100"],"jgt":["E","01101"],
  "je":["E","01111"],"hlt":["F","01010"]}
#label implementation
  
d_labels = {}

for index,line in enumerate(assembly_instructions):
	ls = line.split()
	if ((ls[0][-1] == ':') and ((ls[0][:len(ls[0])-1])not in d_labels)):
		d_labels[(ls[0][:len(ls[0])-1])] = format(index - varlines, '08b')	
  #mov is in both "c" and "b"		

  #testcommit pavit

  #variable assignment function to be inserted here

  #label check niggers
def f_A(a):
	print(d[a[0]][1], end='')
	reg1 = d_registers[a[1]]
	reg2 = d_registers[a[2]]
	reg3 = d_registers[a[3]]
	print('00' + reg1 + reg2 + reg3)

def f_B(a):
	print(d[a[0]][1], end='')
	reg1 = d_registers[a[1]]
	print(reg1 + f'{int(a[2][1:]):08b}')

def f_C(a):
	print(d[a[0]][1], end='')
	reg1 = d_registers[a[1]]
	reg2 = d_registers[a[2]]
	print('00000' + reg1 + reg2 )

def f_D(a):
	print(d[a[0]][1], end='')
	reg1 = d_registers[a[1]]
	reg2 = d_var[a[2]]
	print(reg1 + reg2)

def f_E(a): #label implementation  here <-----
	print(d[a[0]][1], end='')
	reg1 = d_labels[a[1]]
	print('000'+reg1)
def f_F(a):
	print(d[a[0]][1]+"00000000000")

for (index,line) in enumerate(assembly_instructions):
	a = line.split()
	if index in var_index:
		continue

	if a[0] in d.keys():
		if d[a[0]][0] == 'A':
			f_A(a)
		if d[a[0]][0] == 'B':
			f_B(a)
		if d[a[0]][0] == 'C':
			f_C(a)
		if d[a[0]][0] == 'D':
			f_D(a)
		if d[a[0]][0] == 'E': #label implementation here<-----
			f_E(a)
		if d[a[0]][0] == 'F':
			f_F(a)

#label implementation

