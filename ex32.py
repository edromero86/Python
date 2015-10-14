the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
	
# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i
	
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	#append is a function that lists understand
	elements.append(i)  # append function is adding from the list
	
# now we can print them out too
for i in elements:
	print "Element was: %d" % i
	
	
# append() method appends a passed obj into the existing list.


# range()  it generates a list of numbers, which is generally used to iterate over with for loops. 
# There's many use cases. Often you will want to use this when you want to perform an action X number of times, 
# where you may or may not care about the index. 
# Other times you may want to iterate over a list (or another iterable object), 
# while being able to have the index available.

# Python's range() Parameters
# 
# The range() function has two sets of parameters, as follows:
# 
# range(stop)
# 
# stop: Number of integers (whole numbers) to generate, starting from zero. eg. range(3) == [0, 1, 2].
# range([start], stop[, step])
# 
# start: Starting number of the sequence.
# stop: Generate numbers up to, but not including this number.
# step: Difference between each number in the sequence.
