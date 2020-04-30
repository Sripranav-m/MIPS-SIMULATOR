.data
boroque:
	.word 1, 2, 3, 4, 5, 6
done:
	.asciiz "done"
array:
	.word 7, 4, 9, 2, 5, 1, 10, 11, 15, 13, 14 
.text
.globl main
main:
	la $s6,array
	li $s2,0
	li $s3,10
	outerloop:
				li $s1,0
				addi $s2,$s2,1
				beq $s2,$s3,exit
				bne $s2,$s3,innerloop
				j outerloop
	innerloop:  
				beq $s1,$s3,outerloop
				sll $t1,$s1,2
				addi $s1,$s1,1
				sll $t2,$s1,2
				add $t3,$s6,$t1
				add $t4,$s6,$t2
				lw $t5,0($t3)
				lw $t6,0($t4)
				slt $t7,$t5,$t6
				beq $t7,$zero,swap
				
				j innerloop
	swap:
		sw $t5 , 0($t4)
		sw $t6 , 0($t3)
		j innerloop
	exit:
		jr $ra







		