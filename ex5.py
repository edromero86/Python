my_name = 'Edgar Romero'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'white'
my_hair = 'brown'

print "lets talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)
	
# %s, %r, and %d are formatters. They tell python to take the variable on the right and put it in to replace the %s with its value.

# How can I round a floating point number? 
# You can use the round() function like this: round(1.7333)

# %r is good for debugging, and other formats are for actually displaying variables to users. 
# %r it displays the "raw" data of the variable, but we use %s and others for displaying to users. 

#Python Formatters: %s, %r, %d;

# d	Signed integer decimal.	
# i	Signed integer decimal.	
# o	Unsigned octal.	(1)
# u	Unsigned decimal.	
# x	Unsigned hexadecimal (lowercase).	(2)
# X	Unsigned hexadecimal (uppercase).	(2)
# e	Floating point exponential format (lowercase).	
# E	Floating point exponential format (uppercase).	
# f	Floating point decimal format.	
# F	Floating point decimal format.	
# g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.	
# G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.	
# c	Single character (accepts integer or single character string).	
# r	String (converts any python object using repr()).	(3)
# s	String (converts any python object using str()).	(4)
# %	No argument is converted, results in a "%" character in the result.	