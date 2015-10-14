class Parent(object):

	def implicit(self):
		print "PARENT implicit()"
		
class Child(Parent):
	pass
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()


# The use of pass under the class Child: is how you tell python that you want an empty block.
# This creates a class named Child but says that there's nothing new to define in it. 
# Instead, it will inherit all its behavior from Parent. 

# Notice how even through I'm calling son.implicit() on line 13, and even though Child does not have an implicit function defines, it still works and it calls the one defined in Parent.
# This shows that, if you put functions in a base class(Parent), then all subclasses(Child), will automatically get those features. 