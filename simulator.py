instructions=[]
with open("instructions.txt",'r') as f:
    instructions=f.readlines
def add():
def sub():
def mov():
def ld():
def st():
def mul():
def div():
def rs():
def ls():
def xor():
def oor():
def andd():
def nott():
def cmpp():
def jmp():
def jlt():
def jgt():
def je():
def hlt():



d={"add":["A","10000"],"sub":["A","10001"],"mov":["B","10010"],"ld":["D","10100"],"st":["D","10101"],
  "mul":["A","10110"],"div":["C","10111"],"rs":["B","11000"],"ls":["B","11001"],"xor":["A","11010"],"or":["A","11011"],
  "and":["A","11100"],"not":["C","11101"],"cmp":["C","11110"],"jmp":["E","11111"],"jlt":["E","01100"],"jgt":["E","01101"],
  "je":["E","01111"],"hlt":["F","01010"]}  
for i in range(0,len(instructions)):
    opcode=instructions[:5]
    if 
