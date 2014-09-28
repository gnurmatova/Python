import re

while True:
	user_regexp = input("Enter regular expression (enter 'quit' to quit):")
	user_match = input("Enter match text:")
	if(user_regexp == 'quit'):
		break
	regexp = re.compile(user_regexp)
	if(regexp.search(user_match)):
		print("Match found")
	else:
		print("Match is not found")

