def count_by_two(start, end):
	x = start
	#this function assumes that end is bigger than start
	while x < end:
		yield x
		x = x + 2

for i in count_by_two(0, 10):
	print(i)