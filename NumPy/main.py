import numpy as np

# print version of the library or package 
print(np.__version__)


# Analyse the shape of an array
num = np.array([1, 2, 3])

# print the array
print(num)

# print the array shape or dimension
print(num.shape)

# print array data type
print(num.dtype)

# print the array dimension
print(num.ndim)

# print size (total number of elements) of the array
print(num.size)

# print the byte size of data (int64 element has 8 byte)
print(num.itemsize) # each element has 2 byte data size

# change data type of the item/element
# num = num.astype('float64')
num = num.astype('int64')

# access the array element
print(num[0])

# assign the value
# change the value of the element
num[0] = 10
print(num)

# mathematical operation of array
result = num * np.array([2, 0, 4])
print(result)

a = np.array([10, 19, 30, 41, 50, 61])

print(a)

even = np.argwhere(a%2==0).flatten()
print(a[even])