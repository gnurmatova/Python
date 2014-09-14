print("\nAlphabetic Example 2")
names = [["Kim", "Mike", "Alex", "Bob"],["Jim", "John", "Mary"],["Joe", "Tom", "Amy"]]
sortedNames = []
for n in names:
    n.sort()
    sortedNames.append(n)

print(sortedNames)
print(sorted(sortedNames))
