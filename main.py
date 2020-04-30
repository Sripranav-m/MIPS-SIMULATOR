import sys
import instructions
import tkinter
from tkinter.filedialog import askopenfile

window=tkinter.Tk()
window.title("MIPS SIMULATOR")
window.geometry("800x800")

for i in range(0,32):
	stri="btn"+str(i)    
	stri=tkinter.Label(window,text=i)
	stri.grid(column=0,row=i+1)
	str_v_i="btn_v"+str(i)
	str_v_i=tkinter.Label(window,text="0")
	str_v_i.grid(column=1,row=i+1)

def open_file():
	global path_of_file
	if path_of_file:
		print("ERROR... RERUN THE PROGRAM")
	else:
		path_of_file=askopenfile()
		path_of_file=path_of_file.name

def run_program():
	global path_of_file
	global stalls
	global n_ins
	simulate(path_of_file,registers,data_segment_,stalls,n_ins)

menubar=tkinter.Menu(window)
window.config(menu=menubar)
sub_menubar1=tkinter.Menu(menubar,tearoff=False)
menubar.add_cascade(label="FILE",menu=sub_menubar1)
menubar.add_command(label="RUN",command=run_program)
sub_menubar1.add_command(label="open",command=open_file)

path_of_file=""
registers=[0]*32
data_segment_=[]

cycles=0
ipc=0
stalls=0
n_ins=0

for i in range(0,32):
	heading_registers1=tkinter.Label(window,text="register")
	heading_registers1.grid(column=0,row=0)
	heading_registers2=tkinter.Label(window,text="name")
	heading_registers2.grid(column=1,row=0)
	heading_registers3=tkinter.Label(window,text="value")
	heading_registers3.grid(column=2,row=0)
	stri="btn"+str(i)
	stri=tkinter.Label(window,text=i)
	stri.grid(column=0,row=i+1)
	strmi="btnm"+str(i)
	strmi=tkinter.Label(window,text=instructions.get_reg_name(i))
	strmi.grid(column=1,row=i+1)
	str_v_i="btn_v"+str(i)
	str_v_i=tkinter.Label(window,text="0")
	str_v_i.grid(column=2,row=i+1)
	data_heading=tkinter.Label(window,text="data segment")
	data_heading.grid(column=5,row=0)

def simulate(path_of_file,registers,data_segment_,stalls,n_ins):
	data_segment_=[]        
	registers=[0]*32		
	line_number=0			
	asm_file=open(path_of_file,'r')										
	number_of_lines=0			
	with open(path_of_file,'r') as f:
		for line in f:
			number_of_lines+=1					
	asm_file.seek(0,0)
	arr=asm_file.readlines()
	empty_at_last=0
	for iii in range(len(arr),0,-1):
		if ("".join(arr[iii-1].split())) =="\n":
			empty_at_last+=1
		elif ("".join(arr[iii-1].split()))=="":
			empty_at_last+=1
		else:
			break
	asm_file.seek(0,0)
	asm_line=asm_file.readline()
	line_number+=1
	while not asm_line.strip():				
		asm_line=asm_file.readline()
		line_number+=1
	asm_line=asm_file.readline()
	line_number+=1
	while not asm_line.strip():
		asm_line=asm_file.readline()
		line_number+=1
	data_segment={}
	while(".text" not in asm_line):
		val_in_datasegment=asm_file.readline()
		line_number+=1
		while not val_in_datasegment.strip():
			val_in_datasegment=asm_file.readline()
			line_number+=1
		if ".asciiz" in val_in_datasegment:
			val_in_datasegment=val_in_datasegment.split(" ",1)[1]
			val_in_datasegment=val_in_datasegment.split("\"")[1]	
			asm_line="".join(asm_line.split())
			data_segment[asm_line[:-2]]=val_in_datasegment
			data_segment_+=[asm_line[:-1]]
			data_segment_+=[val_in_datasegment]
		elif ".word" in val_in_datasegment:
			val_in_datasegment=val_in_datasegment.split(".word ")[1].split(",")
			for ii in range(0,len(val_in_datasegment)):
				val_in_datasegment[ii]="".join(val_in_datasegment[ii].split())
			new_val_in_datasegment=[]
			for s in val_in_datasegment:
				new_val_in_datasegment.append(int(s))
			data_segment[asm_line[:-2]]=new_val_in_datasegment
			asm_line="".join(asm_line.split())
			data_segment_+=[asm_line[:-1]]
			data_segment_+=new_val_in_datasegment
		asm_line=asm_file.readline()
		line_number+=1
		while not asm_line.strip():
			asm_line=asm_file.readline()
			line_number+=1
	asm_line=asm_file.readline()
	line_number+=1
	while not asm_line.strip():
		asm_line=asm_file.readline()
		line_number+=1
	if ".globl main" not in asm_line:
		print("ERROR  .globl main is not found ")
		sys.exit()  							
	asm_line=asm_file.readline()
	line_number+=1
	while not asm_line.strip():		
		asm_line=asm_file.readline()
		line_number+=1
	if "main:" not in asm_line:
		print("ERROR   main is not found")
		sys.exit()							
	module_line_numbers={'main':line_number}
	asm_line=asm_file.readline()
	line_number+=1
	while not asm_line.strip():		
		asm_line=asm_file.readline()
		line_number+=1
	while line_number < number_of_lines-empty_at_last:
		if ":" in asm_line:
			asm_line=asm_line.split(":")[0]
			asm_line="".join(asm_line.split())
			module_line_numbers[asm_line]=line_number
		asm_line=asm_file.readline()
		line_number+=1
		while not asm_line.strip():
			asm_line=asm_file.readline()
			line_number+=1
	asm_file=open(path_of_file,'r')
	asm_file_lines=asm_file.readlines()
	for i in range(0,len(asm_file_lines)):
		if "#" in asm_file_lines[i]:
			asm_file_lines[i]=asm_file_lines[i].split("#")[0]
		if "$zero" in asm_file_lines[i]:
			asm_file_lines[i]=asm_file_lines[i].replace("$zero","$r0")
	outlist={}
	line_from=module_line_numbers['main']
	i=line_from
	prev_istruction=""
	dep_reg=-1
	while True:
		i+=1
		if "syscall" in asm_file_lines[i-1]:
			if registers[23]==1:
				print(registers[19],end="")
			elif registers[23]==4:
				print(data_segment_[registers[19]],end="")
		instruction=asm_file_lines[i-1].split(" ",1)[0]
		instruction = ''.join(instruction.split())
		if instruction=="li":
			n_ins+=1
			register_name=asm_file_lines[i-1].split(" ",1)[1][:-1]
			register_name=register_name.split(",")
			for ii in range(0,len(register_name)):
				register_name[ii]="".join(register_name[ii].split())
			name=instructions.get_reg_number(register_name[0][:-1],int(register_name[0][-1]))
			instructions.li(registers,int(name),int(register_name[1]))
		elif instruction=="add" or instruction=="sub" or instruction=="slt":
			n_ins+=1
			register_name=asm_file_lines[i-1].split(" ",1)[1][:-1]
			register_name=register_name.split(",")
			for ii in range(0,len(register_name)):
				register_name[ii]="".join(register_name[ii].split())
			name=[0]*3
			name[0]=instructions.get_reg_number(register_name[0][:-1],int(register_name[0][-1]))
			name[1]=instructions.get_reg_number(register_name[1][:-1],int(register_name[1][-1]))
			name[2]=instructions.get_reg_number(register_name[2][:-1],int(register_name[2][-1]))
			name[0]=int(name[0])
			name[1]=int(name[1])
			name[2]=int(name[2])
			if instruction=="add":
				instructions.add(registers,name[0],name[1],name[2],outlist)
			elif instruction=="sub":
				instructions.sub(registers,name[0],name[1],name[2],outlist)
			elif instruction=="slt":
				instructions.slt(registers,name[0],name[1],name[2])
			elif instruction=="and":
				instructions.and_(registers,name[0],name[1],name[2])
			elif instruction=="or":
				instructions.or_(registers,name[0],name[1],name[2])
			elif instruction=="nor":
				instructions.nor_(registers,name[0],name[1],name[2])
			if prev_istruction=="lw":
				if name[1]==dep_reg or name[2]==dep_reg:
					stalls+=1
		elif instruction=="addi" or instruction=="slti" or instruction=="andi" or instruction=="ori":
			n_ins+=1
			register_name=asm_file_lines[i-1].split(" ",1)[1][:-1]
			register_name=register_name.split(",")
			for ii in range(0,len(register_name)):
				register_name[ii]="".join(register_name[ii].split())
			name=[0]*3
			name[0]=instructions.get_reg_number(register_name[0][:-1],int(register_name[0][-1]))
			name[1]=instructions.get_reg_number(register_name[1][:-1],int(register_name[1][-1]))
			name[0]=int(name[0])
			name[1]=int(name[1])
			if instruction=="addi":
				instructions.addi(registers,name[0],name[1],int(register_name[2]))
			elif instruction=="slti":
				instructions.slti(registers,name[0],name[1],int(register_name[2]))
			elif instruction=="andi":
				instructions.andi(registers,name[0],name[1],int(register_name[2]))
			elif instruction=="ori":
				instructions.ori(registers,name[0],name[1],int(register_name[2]))
			if prev_istruction=="lw":
				if name[1]==dep_reg:
					stalls+=1
					
		elif instruction=="bne" or instruction=="beq":
			n_ins+=1
			stalls+=1
			register_name=asm_file_lines[i-1].split(" ",1)[1][:-1]
			register_name=register_name.split(",")
			for ii in range(0,len(register_name)):
				register_name[ii]="".join(register_name[ii].split())
			name=[0]*2
			name[0]=instructions.get_reg_number(register_name[0][:-1],int(register_name[0][-1]))
			name[1]=instructions.get_reg_number(register_name[1][:-1],int(register_name[1][-1]))
			name[0]=int(name[0])
			name[1]=int(name[1])
			if instruction=="bne":
				flagbne=instructions.bne(registers,name[0],name[1])
				if flagbne==1:
					line_from=module_line_numbers[register_name[2]]
					i=line_from
				elif flagbne==0:
					pass
			elif instruction=="beq":
				flagbeq=instructions.beq(registers,name[0],name[1])
				if flagbeq==1:
					line_from=module_line_numbers[register_name[2]]
					i=line_from
				elif flagbeq==0:
					pass
			if prev_istruction=="lw":
				if dep_reg==name[0] or dep_reg==name[1]:
					stalls+=1
		elif instruction=="la":
			n_ins+=1
			register_name=asm_file_lines[i-1].split(" ",1)[1][:-1]
			register_name=register_name.split(",")
			for ii in range(0,len(register_name)):
				register_name[ii]="".join(register_name[ii].split())
			name=instructions.get_reg_number(register_name[0][:-1],int(register_name[0][-1]))
			name=int(name)
			instructions.la(registers,data_segment_,name,register_name[1],outlist)
		elif instruction=="lw" or instruction=="sw":
			n_ins+=1
			register_name=asm_file_lines[i-1].split(" ",1)[1][:-1]
			register_name=register_name.split(",")
			for ii in range(0,len(register_name)):
				register_name[ii]="".join(register_name[ii].split())
			name=instructions.get_reg_number(register_name[0][:-1],int(register_name[0][-1]))
			name=int(name)
			#####
			dep_reg=name
			#####
			s=register_name[1].split("(",1)[0]
			s=int(s)
			r=register_name[1].split("(",1)[1]
			r=r.split(")")[0]
			r="".join(r.split())
			r=instructions.get_reg_number(r[:-1],int(r[-1]))
			if instruction=="lw":
				instructions.lw(registers,data_segment_,name,r,s,outlist)
			elif instruction=="sw":
				instructions.sw(registers,data_segment_,name,r,s,outlist)
		elif instruction=="sll" or instruction=="srl":
			n_ins+=1
			register_name=asm_file_lines[i-1].split(" ",1)[1][:-1]
			register_name=register_name.split(",")
			for ii in range(0,len(register_name)):
				register_name[ii]="".join(register_name[ii].split())
			name=[0]*3
			name[0]=instructions.get_reg_number(register_name[0][:-1],int(register_name[0][-1]))
			name[1]=instructions.get_reg_number(register_name[1][:-1],int(register_name[1][-1]))
			name[0]=int(name[0])
			name[1]=int(name[1])
			if instruction=="sll":
				instructions.sll(registers,name[0],name[1],int(register_name[2]))
			elif instruction=="srl":
				instructions.srl(registers,name[0],name[1],int(register_name[2]))
			if prev_istruction=="lw":
				if dep_reg==name[1]:
					stalls+=1
		elif "jr $ra" in asm_file_lines[i-1]:
			n_ins+=1
			asm_file.close()
			break
		elif "j" in asm_file_lines[i-1]:
			n_ins+=1
			line_from=module_line_numbers[asm_file_lines[i-1].split("j ")[1][:-1]]
			i=line_from
		prev_istruction=instruction
	for i in range(0,32):
		str_v_i="btn_v"+str(i)
		if i in outlist:
			base_add=10010000+(registers[i]*4)
			str_v_i=tkinter.Label(window,text=base_add)
		else:
			str_v_i=tkinter.Label(window,text=registers[i])
		str_v_i.grid(column=2,row=i+1)
	data_heading=tkinter.Label(window,text="data segment")
	data_heading.grid(column=5,row=0)
	data_heading=tkinter.Label(window,text="value")
	data_heading.grid(column=6,row=0)
	for ki in range(0,len(data_segment_)):
		s=tkinter.Label(window,text=str(10010000+(ki*4)))
		s.grid(column=5,row=ki+1)
		s=tkinter.Label(window,text=data_segment_[ki])
		s.grid(column=6,row=ki+1)
	print("********************************")
	print("NUMBER OF STALLS:",end=" ")
	print(stalls)
	print("NUMBER OF INSTRUCTIONS:",end=" ")
	print(n_ins)
	cycles=n_ins+4+stalls
	print("NUMBER OF CYCLES:",end=" ")
	print(cycles)
	print("IPC:",end=" ")
	print(n_ins/cycles)
	print("********************************")

def display_in_gui():
	pass

window.mainloop()