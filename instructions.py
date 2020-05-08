import sys

	
def get_reg_number(reg_alpha,reg_number):
	if reg_alpha=="$s":
		if reg_number>7 or reg_number<0:
			print("ERROR")
			sys.exit()
		return reg_number
	elif reg_alpha=="$t":
		if reg_number>9 or reg_number<0:
			print("ERROR")
			sys.exit()
		return reg_number+8
	elif reg_alpha=="$r":
		if reg_number>0 or reg_number<0:
			print("ERROR")
			sys.exit()
		return 18
	elif reg_alpha=="$a":
		if reg_number>4 or reg_number<0:
			print("ERROR")
			sys.exit()
		return reg_number+19
	elif reg_alpha=="$v":
		if reg_number>1 or reg_number<0:
			print("ERROR")
			sys.exit()
		return reg_number+23
	elif reg_alpha=="$k":
		return reg_number+25
	elif reg_alpha=="$gp":
		return 29
	elif reg_alpha=="$fp":
		return 30
	elif reg_alpha=="$sp":							 
		return 31
	elif reg_alpha=="$ra":
		return 27
	elif reg_alpha=="$at":
		return 28
	
def add(registers,reg1,reg2,reg3,outlist):
	if reg2 in outlist.keys():
		outlist[reg1]=outlist[reg2]
	if reg3 in outlist.keys():
		outlist[reg1]=outlist[reg3]
	registers[reg1]=registers[reg2]+registers[reg3]
def sub(registers,reg1,reg2,reg3,outlist):
	if reg2 in outlist.keys():
		outlist[reg1]=outlist[reg2]
	if reg3 in outlist.keys():
		outlist[reg1]=outlist[reg3]
	registers[reg1]=registers[reg2]-registers[reg3]
def addi(registers,reg1,reg2,val):
	registers[reg1]=registers[reg2]+val
def slt(registers,reg1,reg2,reg3):
	if registers[reg2]<registers[reg3]:
		registers[reg1]=1
	else:
		registers[reg1]=0
def slti(registers,reg1,reg2,val):
	if registers[reg2]<val:
		registers[reg1]=1
	else:
		registers[reg1]=0
def beq(registers,reg1,reg2):
	if registers[reg1]==registers[reg2]:
		return 1	
	return 0
def bne(registers,reg1,reg2):
	if registers[reg1]!=registers[reg2]:
		return 1
	return 0
def la(registers,data_segment,reg1,name,outlist):
	n=data_segment.index(name)
	registers[reg1]=n+1
	outlist[reg1]=n+1
def lw(registers,data_segment,reg1,reg2,shift,outlist):
	n=registers[reg2]-outlist[reg2]
	n=n/4
	n+=(shift/4)
	n+=outlist[reg2]
	n=int(n)
	registers[reg1]=data_segment[n]
def sw(registers,data_segment,reg1,reg2,shift,outlist):
	n=registers[reg2]-outlist[reg2]
	n=n/4
	n+=(shift/4)
	n+=outlist[reg2]
	n=int(n)
	data_segment[n]=registers[reg1]
def li(registers,reg1,value):
	print("************")
	registers[reg1]=value
def sll(registers,reg1,reg2,shift):
	registers[reg1]=registers[reg2]<<shift
def srl(registers,reg1,reg2,shift):
	registers[reg1]=registers[reg2]>>shift
def and_(registers,reg1,reg2,reg3):
	registers[reg1]=registers[reg2]&registers[reg3]
def or_(registers,reg1,reg2,reg3):
	registers[reg1]=registers[reg2]|registers[reg3]
def nor_(registers,reg1,reg2,reg3):
	registers[reg1]=registers[reg2]|registers[reg3]
	registers[reg1]=~(registers[reg1])
def andi(registers,reg1,reg2,val):
	registers[reg1]=registers[reg2]&val
def ori(registers,reg1,reg2,val):
	registers[reg1]=registers[reg2]|val

def get_reg_name(n):
	if n==0:
		return "$s0"
	if n==1:
		return "$s1"
	if n==2:
		return "$s2"
	if n==3:
		return "$s3"
	if n==4:
		return "$s4"
	if n==5:
		return "$s5"
	if n==6:
		return "$s6"
	if n==7:
		return "$s7"
	if n==8:
		return "$t0"
	if n==9:
		return "$t1"
	if n==10:
		return "$t2"
	if n==11:
		return "$t3"
	if n==12:
		return "$t4"
	if n==13:
		return "$t5"
	if n==14:
		return "$t6"
	if n==15:
		return "$t7"
	if n==16:
		return "$t8"
	if n==17:
		return "$t9"
	if n==18:
		return "$r0"
	if n==19:
		return "$a0"
	if n==20:
		return "$a1"
	if n==21:
		return "$a2"
	if n==22:
		return "$a3"
	if n==23:
		return "$v0"
	if n==24:
		return "$v1"
	if n==25:
		return "$k0"
	if n==26:
		return "$k1"
	if n==27:
		return "$ra"
	if n==28:
		return "$at"
	if n==29:
		return "$gp"
	if n==30:
		return "$fp"
	if n==31:
		return "$sp"