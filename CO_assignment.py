import sys
assembly_instructions = []	

for line in sys.stdin:
	if line=="\n":
		pass
	else:
		assembly_instructions.append(line.strip())

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
		if ls[1] in d_var.keys() and error_flag!=0:
			error_flag = 1
			faulty_instructions.append([index+1,":Error redeclaration of variable"])
			#print("Error redeclaration of variable")
	if ls[0]=='var' and index not in var_index:
		error_flag = 1
		faulty_instructions.append([index+1,":Error variable not declared at the beginning"])
		#print("Error variable not declared at the beginning")	

d_registers = {'R0':'000', 'R1':'001', 'R2':'010', 'R3':'011', 'R4':'100', 'R5':'101', 'R6':'110', 'FLAGS':'111'}

d={"add":["A","10000"],"sub":["A","10001"],"mov":["B","10010"],"ld":["D","10100"],"st":["D","10101"],
  "mul":["A","10110"],"div":["C","10111"],"rs":["B","11000"],"ls":["B","11001"],"xor":["A","11010"],"or":["A","11011"],
  "and":["A","11100"],"not":["C","11101"],"cmp":["C","11110"],"jmp":["E","11111"],"jlt":["E","01100"],"jgt":["E","01101"],
  "je":["E","01111"],"hlt":["F","01010"]}
#label implementation
  
d_labels = {}

for index,line in enumerate(assembly_instructions):

	same_loop = 0 #handling re-declaration error

	ls = line.split()
	if ((ls[0][-1] == ':') and ((ls[0][:len(ls[0])-1])not in d_labels)):
		d_labels[(ls[0][:len(ls[0])-1])] = format(index - varlines, '08b')
		same_loop = 1	
	if ((ls[0][-1] == ':') and ((ls[0][:len(ls[0])-1]) in d_labels)) and same_loop!=1:
		error_flag = 1
		faulty_instructions.append([index+1,":Error redeclaration of label found"])
		#print("Error redeclaration of label found")  

  #mov is in both "c" and "b"		

  #testcommit pavit

  #variable assignment function to be inserted here

  #label check niggers
def f_A(a):
	global error_flag
	if 'FLAGS' in a:
		error_flag=1
		faulty_instructions.append([index+1, "Illegal use of flags register"])
	if len(a)!=4:
		error_flag = 1
		faulty_instructions.append([index+1,":Error invalid syntax"])
		#print("Error invalid syntax")
		return
	if a[1] not in d_registers.keys() or a[2] not in d_registers.keys() or a[3] not in d_registers.keys():
		error_flag = 1
		faulty_instructions.append([index+1,":Error invalid register"])
		#print("Error: Invalid Register")
		return
	#conditional statement to check for error flag
	if error_flag == 0:
		load=""
		load+=d[a[0]][1]
		load+="00"
		load+= d_registers[a[1]]
		load+=d_registers[a[2]]
		load+=d_registers[a[3]]
		correct_instructions.append(load)

def f_B(a):
	global error_flag
	if 'FLAGS' in a:
		error_flag=1
		faulty_instructions.append([index+1, "Illegal use of flags register"])
	if len(a)!=3:
		error_flag=1
		faulty_instructions.append([index+1,":Error invalid syntax"])
		#print("Error invalid syntax")
		return
	if a[1] not in d_registers.keys():
		error_flag = 1
		faulty_instructions.append([index+1,":Error invalid register"])
		#print("Error: Invalid Register")
		return	
	if 0<=float(a[2][1:])<=255 and error_flag == 0 and ('.' not in a[2][1:]):
		load=""
		load+=d[a[0]][1]
		load+=d_registers[a[1]]
		load+=f'{int(a[2][1:]):08b}'
		correct_instructions.append(load)
	else:
		error_flag=1
		faulty_instructions.append([index+1,":Error illegal immediate values"])
		#print("Error illegal immidiate values")

def f_C(a):
	global error_flag
	if len(a)!=3:
		error_flag = 1
		faulty_instructions.append([index+1,":Error invalid syntax"])
		#print("Error invalid syntax")
		return
	if a[1] not in d_registers.keys() or a[2] not in d_registers.keys():
		error_flag = 1
		faulty_instructions.append([index+1,":Error invalid register"])
		#print("Error: Invalid Register")
		return
	if a[2] == 'FLAGS':
		error_flag=1
		faulty_instructions.append([index+1, "Illegal use of flags register"])
	if error_flag == 0:	
		load=""	
		if a[0]=="mov":
			load+="10011"
		else:
			load+=d[a[0]][1]
		load+="00000"
		load+= d_registers[a[1]]
		load+= d_registers[a[2]]
		correct_instructions.append(load)

def f_D(a):
	global error_flag
	if 'FLAGS' in a:
		faulty_instructions.append([index+1, "Illegal use of flags register"])
		error_flag=1
	if len(a)!=3:
		error_flag = 1
		faulty_instructions.append([index+1,":Error invalid syntax"])
		#print("Error invalid syntax")
		return
	if a[1] not in d_registers.keys():
		error_flag = 1
		faulty_instructions.append([index+1,":Error invalid register"])
		#print("Error: Invalid Register")
		return
	elif a[2] not in d_var:
		if a[2] in d_labels:
			error_flag = 1
			faulty_instructions.append([index+1,":Error use of label as variable"])
			#print("Error use of label as variable")
		else:
			error_flag = 1
			faulty_instructions.append([index+1,":Error invalid variable"])
			#print("Error: Invalid variable")
		return
	if error_flag == 0:	
		load=""
		load+=d[a[0]][1]
		load+= d_registers[a[1]]
		load+= d_var[a[2]]
		correct_instructions.append(load)

def f_E(a): #label implementation  here <-----
	global error_flag
	if 'FLAGS' in a:
		error_flag = 1
		faulty_instructions.append([index+1, "Illegal use of flags register"])
	if len(a)!=2:
		error_flag = 1
		faulty_instructions.append([index+1,":Error invalid syntax"])
		#print("Error invalid syntax")
		return
	if a[1] not in d_labels:
		if a[1] in d_var:
			error_flag = 1
			faulty_instructions.append([index+1,":Error use of variable as label"])
			#print("Error use of variable as label")
		else:
			error_flag = 1
			faulty_instructions.append([index+1,":Error invalid label"])
			#print("Error: Invalid label")
		return
	if error_flag == 0:
		load=""
		load+=d[a[0]][1]
		load+="000"
		load+= d_labels[a[1]]
		correct_instructions.append(load)


def f_F(a):
	global error_flag
	if 'FLAGS' in a:
		faulty_instructions.append([index+1, "Illegal use of flags register"])
		error_flag = 1
	if len(a)!=1:
		error_flag = 1
		faulty_instructions.append([index+1,":Error invalid syntax"])
		#print("Error invalid syntax")
		return
	
	if error_flag == 0:
		load=""
		load+=d[a[0]][1]+"00000000000"
		correct_instructions.append(load)


if (assembly_instructions[len(assembly_instructions)-1])!="hlt":
    if ((assembly_instructions[len(assembly_instructions)-1]).split())[-1] == "hlt" and  ((assembly_instructions[len(assembly_instructions)-1]).split())[0][-1]==":":
        error_flag = 0
    else:    
        error_flag = 1
        faulty_instructions.append([index+1,":Error last instruction is not halt"])
        #print("Error last instruction is not halt")
	
for (index,line) in enumerate(assembly_instructions):

	if error_flag == 1:
		break

	a = line.split()

	if index>255:
		error_flag = 1
		faulty_instructions.append([index+1,":Error code has exceeded"])
		#print("Error code has exeeded ")
	if index in var_index:
		continue

	if a[0]=="mov":
		if a[-1][0]=="$":
			f_B(a)
		else:
			f_C(a)

	elif (a[0][-1] == ':'):
		label_arr_temp = line.split()[1:]

		if label_arr_temp[0]=="hlt" and (index!=(len(assembly_instructions)-1)):
			error_flag = 1
			faulty_instructions.append([(len(assembly_instructions)-1),"Halt instruction is not the last instruction"])

		if label_arr_temp[0]=="mov":
			if label_arr_temp[-1][0]=="$":
				f_B(label_arr_temp)
			else:
				f_C(label_arr_temp)

		elif label_arr_temp[0] in d.keys():
			if d[label_arr_temp[0]][0] == 'A':
				f_A(label_arr_temp)
			if d[label_arr_temp[0]][0] == 'B':
				f_B(label_arr_temp)
			if d[label_arr_temp[0]][0] == 'C':
				f_C(label_arr_temp)
			if d[label_arr_temp[0]][0] == 'D':
				f_D(label_arr_temp)
			if d[label_arr_temp[0]][0] == 'E': #label implementation here<-----
				f_E(label_arr_temp)

		elif label_arr_temp[0] not in d.keys():
			error_flag = 1
			faulty_instructions.append([index+1,"Error invalid syntax"])
		#print("Error: Invalid Syntax")
		

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
				faulty_instructions.append([index+1,":Error Halt is not being used as the final instruction"])
				#print("Error Halt is not being used as the final instruction")
			f_F(a)
			
	elif a[0] not in d.keys():
		error_flag = 1
		faulty_instructions.append([index+1,"Error invalid syntax"])
		#print("Error: Invalid Syntax")

if error_flag == 1:
	print(f"There is an error in line {faulty_instructions[0][0]}, the error is: {faulty_instructions[0][1]}")
	with open("assembler_faults.txt", "a") as f:
		for line in faulty_instructions:
			f.write(f"There is an error in line {line[0]}, the error is: {line[1]}")
			f.write('\n')		
if error_flag==0:
	for line in correct_instructions:
		print(line)
	for line in correct_instructions:
		with open("assembler_out.txt", "a") as f:
			f.write(line)
			f.write('\n')