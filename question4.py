from glob import glob
import sys
from sys import stdin

import matplotlib.pyplot as plt
import numpy as np

memory=[]
for line in sys.stdin:
	if line=="\n":
		pass
	else:
		memory.append(line.strip())
regs=[0000000000000000,0000000000000000,0000000000000000,0000000000000000,0000000000000000,0000000000000000,0000000000000000,0000000000000000]

x_arr = []
y_arr = []

globalcycle = 0

i_temp = len(memory)

for i in range(i_temp,256):
  memory.append('0000000000000000')

#FLAGS
regs[7]="0000000000000000"

def flag_reset():
  regs[7]="0000000000000000"
  return
  
def set_flag_overflow():
  
  regs[7] = regs[7][:-4] + '1' + regs[7][-3:]
  return

def set_lt_overflow():

  regs[7] = regs[7][:-3] + '1' + regs[7][-2:]
  return

def set_gt_overflow():

  regs[7] = regs[7][:-2] + '1' + regs[7][-1]
  return

def set_equal_overflow():

  regs[7] = regs[7][:-1] + '1'
  return
  

def add(a,b,c):
  regs[c]=regs[a] + regs[b]
  if(regs[c]>2**16-1):
    regs[c] = regs[c]%(2**16 -1)
    set_flag_overflow(regs[7])

def sub(a,b,c):
  regs[c]=regs[a] - regs[b]
  if(regs[c]<0):
    regs[c] = 0
    set_flag_overflow(regs[7])

def movB(a,b):
  regs[a]=b

def movC(a,b):
  if a==7:
    regs[b]=int(regs[a],2)
  else:
    regs[b]=regs[a]

def ld(a,b):
  regs[a]=int(memory[b],2)
  y_arr.append(b)
  global globalcycle
  x_arr.append(globalcycle) 

def st(a,b):
  memory[b]= format(regs[a],'016b')
  y_arr.append(b) 
  global globalcycle
  x_arr.append(globalcycle)

def mul(a,b,c):
  regs[c]=regs[a] * regs[b]
  if regs[c] > (2**16 - 1):
    regs[c] = regs[c]%(2**16-1)
    set_flag_overflow(regs[7])

def div(a,b):
  regs[0]=regs[a]//regs[b]
  regs[1]=regs[a]%regs[b]

def rs(a,b):
  regs[a]=regs[a] // (2**b)

def ls(a,b):
  regs[a]=regs[a] * (2**b)

def xor(a,b,c):
  regs[c]=regs[a] ^ regs[b]   

def oor(a,b,c):
  regs[c]=regs[a] | regs[b]

def andd(a,b,c):
  regs[c]=regs[a] & regs[b]

def nott(a,b):
  regs[b]= 2**16 - regs[a] -1

def cmpp(a,b):
  if regs[a]>regs[b]:
    set_gt_overflow()
  elif regs[a]<regs[b]:
    set_lt_overflow()
  elif regs[a]==regs[b]:
    set_equal_overflow()


d={"10000":"A","10001":"A","10010":"B","10011":"C","10100":"D","10101":"D","10110":"A","10111":"C","11000":"B","11001":"B","11010":"A","11011":"A","11100":"A","11101":"C","11110":"C","11111":"E","01100":"E","01101":"E","01111":"E","01010":"F"}
dfunc={"10000":add,"10001":sub,"10010":movB,"10011":movC,"10100":ld,"10101":st,"10110":mul,"10111":div,"11000":rs,"11001":ls,"11010":xor,"11011":oor,"11100":andd,"11101":nott,"11110":cmpp}

h=len(memory)
ratio=["10001","10000","10110","11110"]
pc=0
while(pc<h):
    hjhj=pc

    globalcycle+=1
    x_arr.append(globalcycle)
    y_arr.append(hjhj)

    opcode=memory[pc][:5]

    if d[opcode]=="A":
      a = int(memory[pc][7:10],2)  
      b = int(memory[pc][10:13],2)
      c = int(memory[pc][13:],2)
      dfunc[opcode](a,b,c)

    elif d[opcode]=="B":
      a=int(memory[pc][5:8],2)
      b=int(memory[pc][8:],2)
      dfunc[opcode](a,b)

    elif d[opcode]=="C":
      a = int(memory[pc][10:13],2)
      b = int(memory[pc][13:],2)
      dfunc[opcode](a,b)

    elif d[opcode]=="D":
      a=int(memory[pc][5:8],2)
      b=int(memory[pc][8:],2)
      dfunc[opcode](a,b)

    elif d[opcode]=="E":
      a=int(memory[pc][8:],2)
      if opcode=="11111":
        pc=a-1
      elif opcode=="01100":
        if regs[7][-3]=="1":
          pc=a-1
      elif opcode=="01101":
        if regs[7][-2]=="1":
          pc=a-1
      elif opcode=="01111":
        if regs[7][-1]=="1":
          pc=a-1
    elif d[opcode]=="F":
      if (opcode not in ratio):
        flag_reset()
    #   print(format(hjhj,'08b'), end=' ')
    #   for j in range(7):
    #     print(format(regs[j],'016b'), end=' ')
    #   print(regs[7])
      break
    if (opcode not in ratio):
      flag_reset()

    # print(format(hjhj,'08b'), end=' ')
    # for hlh in range(7):
    #   print(format(regs[hlh],'016b'), end=' ')
    # print(regs[7])
    pc+=1
    if d[opcode]=="F":
      break

# for i in range (len(memory)):
#   print(memory[i][:16])

plt.scatter(x_arr, y_arr, c='blue')
plt.show()    