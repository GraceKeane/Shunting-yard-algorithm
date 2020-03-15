# Grace Keane - G00359990
# Graph Theory project 2020
# BSc in Computing in Software Development
# The Shunting Yard Algorithm for regular expressions.
	

# The input
infix = "(a|b).c*"

print("Input is:", infix)
	
# Expected output: "ab|c*."
print("Expected:", "ab|c*.")	

# Convert input to a stack list
infix = list(infix)[::-1]	
	
# Operator stack
opers = []
	

# Output list
postfix = []
	
# Operator precidence * - . - |
prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}
	

# Loop through the input one character at a time
while infix:
    # Pop a character from the list
    c = infix.pop() # Removes the last element in infix as a list & returns whatever is poper off
	
    if c == '(':
        # Push an open bracket to the stack
        opers.append(c)
    elif c == ')':
        # Pop operators stack until open bracket is found
	while opers[-1] != '(':
	    postfix.append(opers.pop())
	
	# Remove open bracket
	opers.pop()

    elif c in prec:
	# Push the operator stack until you find an open bracket
	while opers and  prec[c] < prec[opers[-1]]:

	    # Push c to the operator stack with higher precidence to the output
	    postfix.append(opers.push())

            # Push c to the operator stack with higher precidence to the output
            postfix.append(opers.push())
            opers.append(c)
        else:
            # Typically we just push the character to the output
            postfix.append(c)

# Pop all operators to the output
while opers:
    postfix.append(opers.pop())


# Convert output list to string
postfix = ''.join(postfix)


# Print the result
print("Output is: ", postfix)

