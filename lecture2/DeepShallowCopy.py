
import copy

x = [[1,2], [3,4], [5,6]]
y = copy.deepcopy(x)
print("y=",y)
print("x=",x)

x[0][0] = 100
print("y=",y)
print("x=",x)

x[0] = [88,99]
print("y=",y)
print("x=",x)