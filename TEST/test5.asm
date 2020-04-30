.data 
array:
	.word 0, 8, 7, 6, 5, 4, 3, 2, 1, 0
.text
.globl main
main:
	la $s6,array
	li $s0,9
	li $s1,0
	li $s3,1
	loop1:
		li $s2,0
		slt $t0,$s1,$s0
		addi $s1,$s1,1
		beq $t0,$s3,loop2
		bne $t0,$s3,exit
	loop2:
		slt $t1,$s2,$s0
		bne $t1,$s3,loop1
		sll $t2,$s2,2
		add $t3,$t2,$s6
		lw $t4,0($t3)
		lw $t5,4($t3)
		slt $t6,$t4,$t5
		bne $t6,$s3,swap
		addi $s2,$s2,1
		j loop2
	swap:
		sw $t4,4($t3)
		sw $t5,0($t3)
		addi $s2,$s2,1
		j loop2
	exit:
		jr $ra