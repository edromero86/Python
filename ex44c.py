class Parent(object):

	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent()
son = Child()

dad.altered()
son.altered()



# The third wat to use inheritance is a special case of overriding where you want to alter the behavior before or after the Parent class version runs. 
# You first override the function just like in the last example, but then you use a Python built-in function named super to get the Parent version to call. 

# The import lines here are 9-11, where in the Child I do the following when son.altered() is called.
# 1. Because I've overridden Parent.altered the Child.altered version runs, and line 9 executed like you'd expect.
# 2. In this case, I want to do a before and after, so after line 9, I want to use super to get the Parent.altered version. 
# 3. On line 10, I call super(Child, self).altered(), which is a lot like the getattr function you've sued in the past, but it's aware of inheritance and will get the Parent class for you.
# You should be able to read this as "call super with arguments Child and self, then call the function altered on whatever it returns."
# 4. At this point, the Parent.altered version of the function runs, and that prints out the Parent message. 
# 5. Finally, this returns from the Parent.altered, and the Child.altered function continues to print out the after message. 