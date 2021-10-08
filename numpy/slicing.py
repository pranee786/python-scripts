from numpy import *

a1 = arange(3,12)
print(a1)
print(a1[3:7:2])
print(a1[4:])


# Multidimenisonal arrays
a1 = array([1,2,3,4,5,6])
a2 = array([[1,2,3],[4,5,6]])
a3 = array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
print(a1)
print(a2)
print(a3)

# Attributes

print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

print(a1.shape)
print(a2.shape)
print(a3.shape)
a2.shape = (3,2)
print(a2)
a3.shape =(3,3,2)
print(a3)

print(a1.size)
print(a2.size)
print(a3.size)

print(a1.itemsize,a1.dtype)
print(a2.itemsize,a1.dtype)
print(a3.itemsize,a1.dtype)

print(a1.nbytes)
print(a2.nbytes)
print(a3.nbytes)
