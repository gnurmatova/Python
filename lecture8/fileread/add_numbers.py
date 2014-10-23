fileName = input("Enter the file name:")
total = 0
try:
	with open(fileName) as f:
	
		while(True):
			l = f.readline()
			if(not l):
				break
			total += int(l)
	
except ValueError:
	print("Value error:", l.strip(), " is not a number")
except FileNotFoundError:
	print("Could not find file:", fileName)

print("The total is:", total)