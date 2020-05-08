ins_3comp = ["add","sub","bne","beq","slt"]
ins_3comp_imm = ["addi","slti","sll"]
ins_2comp = ["lw","sw","mov"]
ins_2comp_imm = ["li",,"la"]
ins_1comp = ["j","jr"]		

ip = p
count = 0

insf_insd = []
insd_ex = []
ex_mem = []
mem_wb = []

ins_fetch = 1
ins_decode = 0
execute = 0
memory_stage = 0
writeback = 0
 

jr = 0
cycles = 0
clock = 0
stalls = 0
stall_detected = 0
stall_detected_control = 0
memory_stage_visited = 0

# Executing the instructions given below main: 
# ip is instruction pointer which is the index of the list containing all the instructions 
# ip goes till length of s

while true:  
	# ip<len(s)-1 
	# ip = ip + 1

	if (s[ip]==["",""]):  # Skipping if any new lines are present in my assembly file
		continue 
	else:
		cycles = cycles + 1

		if writeback == 1:
		#code for writeback
		# enable memory_stage
		#make writeback =0

		elif memory_stage == 1:
		#code for memory stage
		# enable execute and writeback
		#make memory_stage =0

		elif execute == 1:
		#  Code for execute
		#enable memory and ins decode
		#make execute = 0

		elif ins_decode == 1:

			print("Instruction Decoded  "+insf_insd[0])

			if insf_insd[0] in ins_3comp:
				if insf_insd[0] == "bne":
					index1 = check_s_or_t(insf_insd[1])
					index2 = check_s_or_t(insf_insd[2])
					operand1 = reg[index1]
					operand2 = reg[index2]
					if operand2 != operand1:
						insd_ex = [insf_insd[0],insf_insd[3],"false"]
						stalls = stalls + 1
						stall_detected_control = 1
						ip = jump(insf_insd[3]) + 1


					else:
						insd_ex = [insf_insd[0],insf_insd[3],"true"]
					 
				elif insf_insd[0] == "beq":
					index1 = check_s_or_t(insf_insd[1])
					index2 = check_s_or_t(insf_insd[2])
					operand1 = reg[index1]
					operand2 = reg[index2]
					if operand2 == operand1:
						insd_ex = [insf_insd[0],insf_insd[3],"false"]
						stalls = stalls + 1
						stall_detected_control = 1
						ip = jump(insf_insd[3]) + 1

					else:
						insd_ex = [insf_insd[0],insf_insd[3],"true"]
					 
				else:
					index2 = check_s_or_t(insf_insd[2])
					index3 = check_s_or_t(insf_insd[3])
					operand1 = reg[index2]
					operand2 = reg[index3]
					insd_ex = [insf_insd[0],insf_insd[1],insf_insd[2],insf_insd[3],operand1,operand2]

			elif insf_insd[0] in ins_3comp_imm:
				index = check_s_or_t(insf_insd[2])
				operand1 = reg[index]
				insd_ex = [insf_insd[0],insf_insd[1],insf_insd[2],operand1,int(insf_insd[3])]

			elif insf_insd[0] in ins_2comp:
				if insf_insd[0] == "lw":
					b = insf_insd[2]
					c = insf_insd[2]
					c = c.remove(" ","")
					index = check_s_or_t(b[0:-1])
					operand1 = reg[index] 
					b = b.split('(')[0]
					offset = int(b)
					insd_ex = [insf_insd[0],insf_insd[1],c[-4:-1],operand1,offset]
				elif insf_insd[0] == "sw":
					b = insf_insd[2]
					c = insf_insd[2]
					c = c.remove(" ","")
					index = check_s_or_t(b[0:-1])
					index1 = check_s_or_t(insf_insd[1])
					operand2 = reg[index]
					operand1 = reg[index1] 
					b = b.split('(')[0]
					offset = int(b)
					insd_ex = [insf_insd[0],insf_insd[1],c[-4:-1],operand1,operand2,offset]
				else:
					index = check_s_or_t(insf_insd[2])
					operand = reg[index]
					insd_ex = [insf_insd[0],insf_insd[1],operand,insf_insd[2]]

			elif insf_insd[0] in ins_2comp_imm:
				insd_ex = insf_insd

			elif insf_insd[0] in ins_1comp:
				if insf_insd[0] == "j":
					stalls = stalls + 1
					stall_detected_control = 1
					ip = jump(insf_insd[1]) + 1



					insd_ex = insf_insd

				elif insf_insd[0] == "jr":
					insd_ex = insf_insd
					jr = 1
					
					

			if jr == 1:
				ins_fetch = 0
				execute = 1
				ins_decode = 0
			if stall_detected_control == 1:
				ins_fetch = 0
				execute = 1
				ins_decode = 0
			else:
				ins_fetch = 1
				execute = 1
				ins_decode = 0


		elif ins_fetch == 1:
			insf_insd = s[ip]
			print("Instruction Fetched")
			print("")
			ip = ip+1
			ins_decode = 1
			ins_fetch = 0

		#update all latches
		ex_mem = temp_ex_mem

