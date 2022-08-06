import sys
from sys import stdin
def braaah(number):
    x=number-int(number)
    while(x-int(x)!=0):
        x=x*2
    x=int(x)
    number=int(number)
    ban=""
    ll1=len(bin(number).replace("0b", ""))
    ll2=len(bin(x).replace("0b",""))
    ll1=ll1-1
    ban+=bin(number).replace("0b", "")
    ban=ban[1:]
    ban+=bin(x).replace("0b","")
    if(len(ban)<=5):
        while(len(ban)<5):
            ban+='0'
        if ll1>7:
            return -1
        else:
            ban=f'{ll1:03b}'+ban
            ban="00000000"+ban
            return(ban)
    else:
        return -1
def revrsenatty(b):
    exp=b[0:3]
    llj=int(exp,2)
    mant=b[3:]
    jk=int(mant,2)/32
    jk+=1
    jk*=2**(llj)
    return(jk)

memory=[]
for line in sys.stdin:
	if line=="\n":
		pass
	else:
		memory.append(line.strip())
regs=[0000000000000000,0000000000000000,0000000000000000,0000000000000000,0000000000000000,0000000000000000,0000000000000000,0000000000000000]

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

def st(a,b):
  memory[b]= format(regs[a],'016b')

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

def f_add(a,b,c):
  regs[c]=regs[a]+regs[b]
  if (braaah(regs[c])==-1):
    regs[c]=0
    set_flag_overflow()
def f_sub(a,b,c):
  regs[c]=regs[a]+regs[b]
  if (regs[c]<0 or braaah(regs[c])==-1):
    regs[c]=0
    set_flag_overflow()
def movf(a,val):
  regs[a]=val

d={"00000":"A","00001":"A","00010":"B","10000":"A","10001":"A","10010":"B","10011":"C","10100":"D","10101":"D","10110":"A","10111":"C","11000":"B","11001":"B","11010":"A","11011":"A","11100":"A","11101":"C","11110":"C","11111":"E","01100":"E","01101":"E","01111":"E","01010":"F"}
dfunc={"00000":f_add,"00001":f_sub,"10000":add,"10001":sub,"10010":movB,"10011":movC,"10100":ld,"10101":st,"10110":mul,"10111":div,"11000":rs,"11001":ls,"11010":xor,"11011":oor,"11100":andd,"11101":nott,"11110":cmpp}


h=len(memory)
ratio=["10001","10000","10110","11110"]
pc=0
while(pc<h):
    hjhj=pc
    opcode=memory[pc][:5]
    if d[opcode]=="A":
      a = int(memory[pc][7:10],2)  
      b = int(memory[pc][10:13],2)
      c = int(memory[pc][13:],2)
      dfunc[opcode](a,b,c)

    elif d[opcode]=="B":
      a=int(memory[i][5:8],2)
      if opcode=="00010":
        b=revrsenatty[8:]
        movf(a,b)
      else:
        b=int(memory[i][8:],2)
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
      print(format(hjhj,'08b'), end=' ')
      for j in range(7):
        if regs[j]-int(regs[j])==0:
            print(format(int(regs[j]),'016b'), end=' ')
        else:
            print(braaah(regs[j]))
      print(regs[7])
      break
    if (opcode not in ratio):
      flag_reset()

    print(format(hjhj,'08b'), end=' ')
    for hlh in range(7):
      print(format(regs[hlh],'016b'), end=' ')
    print(regs[7])
    pc+=1
    if d[opcode]=="F":
      break

for i in range (len(memory)):
  print(memory[i][:16])