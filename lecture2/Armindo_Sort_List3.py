print("\nAlphabetic Example 2")
names = [["Kim", "Mike", "Alex", "Bob"],["Jim", "John", "Mary"],["Joe", "Tom", "Amy"]]

print("initial list:")
print(names)
print("_____________")

sortedNames = []
for n in names:
    n.sort()
    sortedNames.append(n)

print("each sub-list is sorted individually:")
print(sortedNames)
print("_____________")

print("entire list is sorted at once:")
print(sorted(sortedNames))
