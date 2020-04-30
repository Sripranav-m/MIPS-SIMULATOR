.data 
array:
	.word 3, 4, 7, 2
.text
.globl main
main:
	la $s6,array
	li $t1,4
	li $t0,0
	loop:
		beq $t0,$t1,exit
		sll $t4,$t0,2
		add $t3,$s6,$t4
		addi $t0,$t0,1
		lw $s0,0($t3)
		j loop
	exit:
		jr $ra