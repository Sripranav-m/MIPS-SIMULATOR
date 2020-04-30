.data
array:
	.word 3, 4, 5, 6
.text
.globl main
main:
	la $s6,array
	lw $s0,8($s6)
	lw $s1,4($s6)
	sw $s1,8($s6)
	sw $s0,4($s6)
	bne $s1,$s0,exit

exit:
	jr $ra