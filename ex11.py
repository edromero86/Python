print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)


# Notice that we put a , (comma) at the end of each print line. 
# This is so that print doesn't end the line with a new line character and go to the next line. 


# How to get a number from user to do math:
# x = int(raw_input()), which gets the number as a string then converts it to an integer.