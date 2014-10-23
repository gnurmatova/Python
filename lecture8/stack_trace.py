def function3(param3):
	print("in function3")
	try:
		raise SyntaxError("ERROR:"+param3)
	except:
		pass
	print("after exception 3")

def function2(param2):
	print("in function2")
	function3(param2)
	print("after exception 2")

def function1(param1):
	print("in function1")
	function2(param1)
	print("after exception 1")

try:
	function1("Test")
except:
	print("caught at main")