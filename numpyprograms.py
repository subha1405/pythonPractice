# importing numpy
import numpy as np

# creating an array
a=np.array([11,2,3,4])

# printing the array
print(a[0])

# checking dimension of the array
print(a.ndim)

# Creating an multidimensional array
b=np.array([[1,4,56,5],[2,5,3,7,]])
print(b)
print(b.ndim)


# slicing an array
print(a[1:2])
print(a[1:])
print(a[-1:])
print(a[-3:3])
print(a[0:0])

