def modifyValues(int1, str1, list1):
	int1=1000
	str1="1000"
	list1=[1000, 1000, 1000]
	print("Inside Function:")
	print("int1", int1)
	print("str1", str1)
	print("list1", list1)
	print("_________________")

int1=1
str1="1"
list1=[1,1,1]

modifyValues(int1, str1, list1)

print("Outside Function:")
print("int1", int1)
print("str1", str1)
print("list1", list1)
print("_________________")