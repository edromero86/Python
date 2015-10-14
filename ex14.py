from sys import argv

script, user_name = argv
prompt = '> '    # I can use any character I like for '> '. # $ * etc..

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions?"
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)



# Notice though that we make a variable prompt that is set tot the prompt we want, 
# and we give that to raw_input instead of typing it over and over. 