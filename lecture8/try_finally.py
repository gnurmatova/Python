try:
	raise SyntaxError("my own error")
except ZeroDivisionError:
	print("caught division by zero")
except SyntaxError:
	print("caught syntax error")
else:
	print("in else block")
finally:
	print("in finally block")
