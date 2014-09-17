def f_a(param1):
	return param1
	
def f_b(param2):
	return param2

f1 = f_a
print(f1(3))

fm = (f_a, f_b)
print(fm[1](4))

