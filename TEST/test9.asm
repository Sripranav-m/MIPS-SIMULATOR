.data
array:	
	.word 3, 3, 4, 3
tirutsava:
	.asciiz "Tirutsava 2020\n"
value:
	.asciiz "Value of i is: "
.text
.globl main
main:
	la $s6,array
	li $s5,				3
	li $s3,		0
	Loop: 



		sll $t1, $s3, 2
		add $t1,$t1,$s6
		lw $t0, 0($t1)
		bne $t0, $s5, Exit
		addi $s3, $s3, 2
		j Loop
	Exit: 
	li $v0, 4           	
	la $a0, tirutsava 	
	syscall
	li $v0, 4           	
	la $a0, 	value 	
	syscall
	li $v0, 	1
	add $a0,	$zero,$s3
	syscall
	jr $ra




