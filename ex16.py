from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTR-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') #  open the file in write mode. 

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for the three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm goint to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()


# if you type in terminal cat test.txt, you will be able to view your new three files that were written. 


# functions/methods
# 
# close : closes the file. Like file -> save.. in your editor. 
# read : reads the contents of the file. You can assign the result to avariable. 
# realine : reads just one line of a text file.
# truncate : empties the file. Watch out if you care about the file. 
# write(stuff) : writes stuff to the file. 

# What does 'w' mean? a string character in it for the kind of mode for the file. 
# 'w' -> open the file in write mode. 
# 'r' -> read
# 'a' -> append


# 'w+' 'r+' 'a+' -> This will open the file in both read and write mode and,
# depending on the character used, position the file in different ways. 