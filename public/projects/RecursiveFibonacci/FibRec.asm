# FibRec.asm
# This program computes the nth fibonacci number recursively.

	.data
n:	.word	10			# n


	.text
		
Main:

	lw	$t0, n			# Reading n from memory into $t0
	add	$a0, $t0, $zero		# Copy n from $t0 to $a0
	jal	fibRec			# Call fib
	j	Exit			# Exit program



fibRec:

	addi	$sp, $sp, -8		# push data onto stack
	sw	$ra, 4($sp)
	sw	$a0, 0($sp)
	
	beq	$a0, 1, baseRet		# if(n==1) return 0
	beq	$a0, 2, baseTwoRet	# if(n==2) return 1
	
fibRecCase:

	addi	$a0, $a0, -1		# n-1
	jal	fibRec			# fibRec(n-1)
	
					# add here
	addi	$a0, $a0, -1		# n-2 (because n-1 already happened)
	jal	fibRec			# fibRec(n-2)
	
	lw	$ra, 4($sp)		# pop data from the stack
	lw	$a0, 0($sp)
	addi	$sp, $sp, 8
	
	jr	$ra			# Return from this case
	
baseRet:

	add	$v0, $v0, $zero		# Return value set to zero
	
	lw	$ra, 4($sp)		# pop data off of stack
	lw	$a0, 0($sp)
	addi	$sp, $sp, 8
	
	jr	$ra			# Return
	
baseTwoRet:

	addi	$v0, $v0, 1		# Return value set to 1
	
	lw	$ra, 4($sp)		# pop data off of stack
	lw	$a0, 0($sp)
	addi	$sp, $sp, 8
	
	jr	$ra			# Return



Exit:
