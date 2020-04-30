.data 
array:
	.word 3, 4, 7, 2
.text
.globl main
main:
	la $s6,array
	li $s0,0
	li $s1,3
	li $s3,1
	loop:
		beq $s0,$s1,exit
		sll $t4,$s0,2
		addi $s0,$s0,1
		add $t3,$s6,$t4
		lw $t0,0($t3)
		lw $t1,4($t3)
		slt $t5,$t0,$t1
		beq $t5,$s3,swap
		j loop

	swap:
		sw $t1,0($t3)
		sw $t0,4($t3)
		j loop

	exit:
		jr $ra