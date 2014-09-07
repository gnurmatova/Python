def custom_sort(str1):
	return len(str1)

x=["melon", "apple", "banana", "Apricot"]

print("Python Default Sort:")
x.sort()
print(x)

print("Custom Sort:")
x.sort(key=custom_sort)
print(x)

print("Custom Sort:")
x.sort(key=custom_sort)
print(x)

print("Reverse Sort:")
x.sort(key=custom_sort, reverse=True)
print(x)