age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)



# raw_input(...)
#     raw_input([prompt]) -> string
#     
#     Read a string from standard input.  The trailing newline is stripped.
#     If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
#     On Unix, GNU readline is used if enabled.  The prompt string, if given,
#     is printed without a trailing newline before reading.

# The pydoc module automatically generates documentation from Python modules. 
# The documentation can be presented as pages of text on the console, 
# served to a Web browser, or saved to HTML files.