.data
array:
	.word 3, 4, 7, 2
.text
.globl main
main:

	li $t0,4
	li $t1,5
	li $t3,0

	add $s0,$t0,$zero
	sub $s1,$t1,$zero

	slt $s2,$zero,$t0


	jr $ra