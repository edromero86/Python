from sys import argv  # sys is a package, and this phrase just says to get the argv features from that package.

script, filename = argv

txt = open(filename)  # open function opens the file with parameter.

print "Here's your file %r:" % filename
print txt.read()    # read function read the file. 

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()



# Line 5 we use a new command 'open' which opens a file. 

# line 8 we call a function on txt. 

# You give a file function by using the .(dot or period), the name of the function, and parameters.

# The difference is that when you say txt.read() you are saying, 
# Hey txt, do your read function with no parameters. 