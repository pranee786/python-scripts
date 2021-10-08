from numpy import *

a1 = arange(12)
print(a1)
a2 = reshape(a1,(2,6))
print(a2)
a3 = reshape(a1,(4,3))
print(a3)
a4 = reshape(a1,(2,2,3))
print(a4)

print(a4.flatten())
print(eye(3))
print(eye(2))
print(ones((2,3),int))
print(zeros((2,3),int))
