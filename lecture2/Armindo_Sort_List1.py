z = [[1,3],[5,4],[1,2],[3,4,1,7,2,9]]
print("Initial z:")
print(z)
print("__________")

# Sort a specific element
print("Sorted z[3] using sorted():")
print(sorted(z[3]))
print("__________")

# Sort all elements, then sort the data inside each element. 
z.sort()
print("Sorted z, using sort() method:")
print(z)
print("__________")

print("Sorted z, using sorted() function:")
for l in z:
    print(sorted(l))