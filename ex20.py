from sys import argv

script, input_file = argv 

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)   # seek() sets the fil's current position at the offset. The Whence argument is optional and defaults to 0 
		
def print_a_line(line_count, f):
	print line_count, f.readline()  # readline() reads the entire line from  the file. 
	
current_file = open(input_file)

print "First let's orint the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)		


# seek() sets the fil's current position at the offset. The Whence argument is optional and defaults to 0, 
# which means absolute file positioning, other values are 1 which means seek relative to the current position,
# and 2 means seek relative to the file's end. seek() function is dealing in bytes. 

# readline() reads the entire line from  the file. 