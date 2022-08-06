import math

d={"kB":2**13,"MB":2**23,"GB":2**33,"kb":2**10,"Mb":2**20,"Gb":2**30}
mem=input("Enter the space in memory(space separated ): ")

print("1. Bit Addressable Memory - Cell Size = 1 bit\n2. Nibble Addressable Memory - Cell Size = 4 bit\n3. Byte Addressable Memory - Cell Size = 8 bits(standard)\n4. Word Addressable Memory - Cell Size = Word Size (depends on CPU)\n")
addr=input("Enter Memory address type: ")

bit=int(input("\nEnter length of instruction in bits: "))
reg=int(input("\nEnter length of register in bits: "))

inst= bit * d[mem[-2::]] * int(mem.split()[0])
inst_final= int(math.log(inst,2))

print("\nMinimum bits needed to represent the address: ",inst_final)

if(reg>=inst_final):
    print("Error:Cant support any register")
    exit()

elif(inst_final-reg>=6):
    opcode_a=5
    p_bit=inst_final-reg-opcode_a

elif(inst_final-reg>=4 and inst_final-reg<=5):
    opcode_a=3
    p_bit=inst_final-reg-opcode_a

#TYPE-A
print("\nType-A opcode bits: ",opcode_a)
print("Type-A P-bit address bits: ",p_bit)
print("Type-A reg address bits: ",reg)
print("No of instructions Type-A ISA supports: ",2**opcode_a)
print("No of registers Type-A ISA supports: ",2**reg)

if(2*reg>=inst_final):
    print("Error:Cant support any register")
    exit()

elif(inst_final-2*reg>=6):
    opcode_b=5
    r_bit=inst_final-2*reg-opcode_b

elif(inst_final-2*reg>=4 and inst_final-2*reg<=5):
    opcode_b=3
    r_bit=inst_final-2*reg-opcode_b

#TYPE-B
print("\nType-B opcode bits: ",opcode_b)
print("Type-B R-bit filler bits: ",r_bit)
print("Type-B reg address bits: ",2*reg)
print("No of instructions Type-B ISA supports: ",2**opcode_b)
print("No of registers Type-B ISA supports: ",2**reg)


#TYPE-1
cpu=int(input("\nEnter the CPU bit(TYPE-1): "))
convert=input("Enter the new addressable memory: ")

d2={"bit addressable memory":1,"nibble addressable memory":4,"byte addressable memory":8,"word addressable memory":cpu}

total_mem= d[mem[-2::]] * int(mem.split()[0])
x=convert.lower()
y=addr.lower()
type1_final= int(math.log(total_mem/int(d2[x]),2) - math.log(total_mem/int(d2[y]),2)) 
print("\nPins Saved: ",type1_final)

#TYPE-2
cpu2=int(input("\nEnter the CPU bit(TYPE-2): "))
cpu_byte=cpu2//8
pins=int(input("Enter address pins: "))
addr2=input("Enter memory address type: ")
if(addr2.lower()!="word addressable memory"):
    if(pins>30):
        print("Main memory Bytes: ",2**(pins-30),"GB")
    elif(pins>20 and pins<=30):
        print("Main memory Bytes: ",2**(pins-20),"MB")
    elif(pins>10 and pins<=20):
        print("Main memory Bytes: ",2**(pins-10),"KB")
    elif(pins>0 and pins<=10):
        print("Main memory Bytes: ",2**(pins-0),"B")
    else:
        print("ZERO MEMORY")

else:
    if(pins>30):
        print("Main memory Bytes: ",cpu_byte*2**(pins-30),"GB")
    elif(pins>20 and pins<=30):
        print("Main memory Bytes: ",cpu_byte*2**(pins-20),"MB")
    elif(pins>10 and pins<=20):
        print("Main memory Bytes: ",cpu_byte*2**(pins-10),"KB")
    elif(pins>0 and pins<=10):
        print("Main memory Bytes: ",cpu_byte*2**(pins-0),"B")
    else:
        print("ZERO MEMORY")








    

