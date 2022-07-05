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

#making a flag to check for errors

error_flag = 0

#flag set to 0 initially, value will be changed to 1 in case of an error

for index,line in enumerate(assembly_instructions):
	ls = line.split()
	if ls[0]=='var' and index in var_index:
		if ls[1] not in d_var.keys():
			d_var[ls[1]] = format(var_val, '08b')
			var_val+=1
		if ls[1] in d_var.keys():
			error_flag = 1
			#print("Error redeclaration of variable")
	if ls[0]=='var' and index not in var_index:
		error_flag = 1
		#print("Error variable not declared at the beginning")


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
	if ((ls[0][-1] == ':') and ((ls[0][:len(ls[0])-1]) in d_labels)):
		error_flag = 1
		#print("Error redeclaration of label found")
  
  
  #mov is in both "c" and "b"		

  #testcommit pavit

  #variable assignment function to be inserted here

  #label check niggers
def f_A(a):
	global error_flag
	if len(a)!=4:
		error_flag = 1
		#print("Error invalid syntax")
		return
	if a[1] not in d_registers.keys() or a[2] not in d_registers.keys() or a[3] not in d_registers.keys():
		error_flag = 1
		#print("Error: Invalid Register")
		return
	#conditional statement to check for error flag
	if error_flag == 0:
		print(d[a[0]][1], end='')
		reg1 = d_registers[a[1]]
		reg2 = d_registers[a[2]]
		reg3 = d_registers[a[3]]
		print('00' + reg1 + reg2 + reg3)

def f_B(a):
	global error_flag
	if len(a)!=2:
		error_flag=1
		#print("Error invalid syntax")
		return
	if a[1] not in d_registers.keys():
		error_flag = 1
		#print("Error: Invalid Register")
		return
	if int(a[2][1:])<=255 and error_flag == 0:
		print(d[a[0]][1], end='')
		reg1 = d_registers[a[1]]
		print(reg1 + f'{int(a[2][1:]):08b}')
	else:
		error_flag=1
		#print("Error illegal immidiate values")

def f_C(a):
	global error_flag
	if len(a)!=3:
		error_flag = 1
		#print("Error invalid syntax")
		return
	if a[1] not in d_registers.keys() or a[2] not in d_registers.keys():
		error_flag = 1
		#print("Error: Invalid Register")
		return
	if error_flag == 0:		
		if a[0]=="mov":
			print("10011", end='')
		else:
			print(d[a[0]][1], end='')
		reg1 = d_registers[a[1]]
		reg2 = d_registers[a[2]]
		print('00000' + reg1 + reg2 )

def f_D(a):
	global error_flag
	if len(a)!=3:
		error_flag = 1
		#print("Error invalid syntax")
		return
	if a[1] not in d_registers.keys():
		error_flag = 1
		#print("Error: Invalid Register")
		return
	elif a[2] not in d_var:
		if a[2] in d_labels:
			error_flag = 1
			#print("Error use of label as variable")
		else:
			error_flag = 1
			#print("Error: Invalid variable")
		return
	if error_flag == 0:	
		print(d[a[0]][1], end='')
		reg1 = d_registers[a[1]]
		reg2 = d_var[a[2]]
		print(reg1 + reg2)

def f_E(a): #label implementation  here <-----
	global error_flag
	if len(a)!=2:
		error_flag = 1
		#print("Error invalid syntax")
		return
	if a[1] not in d_labels:
		if a[2] in d_var:
			error_flag = 1
			#print("Error use of variable as label")
		else:
			error_flag = 1
			#print("Error: Invalid label")
		return
	if error_flag == 0:
		print(d[a[0]][1], end='')
		reg1 = d_labels[a[1]]
		print('000'+reg1)


def f_F(a):
	global error_flag
	if len(a)!=1:
		error_flag = 1
		#print("Error invalid syntax")
		return
	
	if error_flag == 0:
		print(d[a[0]][1]+"00000000000")

if assembly_instructions[len(assembly_instructions)-1]!="hlt":
	error_flag = 1
	#print("Error last instruction is not halt")		

for (index,line) in enumerate(assembly_instructions):

	if error_flag == 1:
		break

	a = line.split()
	if index>255:
		error_flag = 1
		#print("Error code has exeeded ")
	if index in var_index:
		continue
	if a[0]=="mov":
		if a[-1][0]=="$":
			f_B(a)
		else:
			f_C(a)
	elif a[0] in d.keys():
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
			if index!=len(assembly_instructions)-1:
				error_flag = 1
				#print("Error Halt is not being used as the final instruction")
			f_F(a)
	elif a[0] not in d.keys():
		error_flag = 1
		#print("Error: Invalid Syntax")