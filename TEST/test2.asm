.data 
array:
	.word 3, 4, 7, 2
.text
.globl main
main:
	la $s6,array
	li $s0,0
	li $s1,3
	loop:
		beq $s0,$s1,exit
		sll $t1,$s0,2
		addi $s0,$s0,1
		add $t3,$s6,$t1
		lw $t0,0($t3)
		addi $t0,$t0,1
		sw $t0,0($t3)
		j loop
	exit:
		jr $ra