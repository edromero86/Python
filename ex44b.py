class Parent(object):

	def override(self):
		print "PARENT override()"
		
class Child(Parent):

	def override(self):
		print "CHILD override()"
		
dad = Parent()
son = Child()

dad.override()
son.override()

# The problem with implicitly having functions called is sometimes you want the child to behave differently. 
# In this case, you want to override the function child, effectively replacing the functionality. 
# To do this, just define a function with the same name in Child. 

# As you can see, when line 14 runs, it runs the Parent.override function because that variable (dad) is a Parent.
# But when line 15 runs, it prints out the Child.override messages because son is an instance of Child and Child overrides that function by defining its own version. 