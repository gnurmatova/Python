d1 = {
"lambda1": lambda p1, p2: p1 + p2,
"lambda2": lambda p1, p2: p1 - p2
}

print(d1["lambda1"](5, 4))
print(d1["lambda2"](5, 4))
