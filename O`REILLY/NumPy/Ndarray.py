
import numpy as np
from numpy.matlib import randn

data = [[0.9526, -0.246, -0.8856], [0.5639, 0.2379, 0.9104]]
data = np.array(data)

print(data)

print(data*10)

print(data + data)

print(data.shape)
print(data.dtype)


#####################
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

print(arr1)


#####################

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)

print(arr2)
print(arr2.ndim)
print(arr2.shape)

#####################

print(np.zeros(10))
print(np.zeros((3, 6)))
print(np.empty((2, 3, 2)))
print(np.arange(15))

#####################

#Data Types for ndarrays

arr1 = np.array([1, 2, 3], dtype = np.float64)
arr2 = np.array([1, 2, 3], dtype = np.int32)


#To convert
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)

float_arr = arr.astype(np.float64)
print(float_arr.dtype)


arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)

print(arr.astype(np.int32))


numeric_strings = np.array(['1.25', '-9.6', '42'], dtype = np.string_)
print(numeric_strings.astype(float))

#####################

int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype = np.float)
print(int_array.astype(calibers.dtype))


empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)




#####################

#Operations between Arrays and Scalars

arr = np.array([[1., 2., 3.],[4., 5., 6.]])
print(arr)
print(arr*arr)
print(arr - arr)

print(1 / arr)
print(arr ** 0.5)



#Basic Indexing and Slicing

arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])

arr[5:8] = 12
print(arr)



arr_slice = arr[5:8]

arr_slice[1] = 12345
print(arr)

arr_slice[:] = 64
print(arr)


#####################

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])

print(arr2d[0][2])
print(arr2d[0, 2])



arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [7, 8, 9], [10, 11, 12]])

print(arr3d)
print(arr3d[0])

old_values = arr3d[0].copy()

arr3d[0] = 42
print(arr3d)

arr3d[0] = old_values
print(arr3d)

print(arr3d[1, 0])

#Indexing with slices

print(arr[1:6])
print(arr2d)
print(arr2d[:2])

print(arr2d[:2, 1:])

print(arr2d[1, :2])
print(arr2d[2, :1])
print(arr2d[:, :1])


#Boolean Indexing

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = randn(7,4)

print(names == 'Bob')
print(data[names == 'Bob'])
print(data[names == 'Bob', 2:])
print(data[names == 'Bob', 3])

print(names != 'Bob')

print(data[-(names == 'Bob')])


mask = (names == 'Bob') | (names == 'Will')
print(mask)

print(data[mask])

data[data < 0] = 0

print(data)

data[names != 'Joe'] = 7
print(data)



#Fancy Indexing

arr = np.empty((8, 4))

for i in range(8):
    arr[i] = i

print(arr)

print(arr[[4, 3, 0, 6]])
print(arr[[-3, -5, -7]])


#####################

arr = np.arange(32).reshape((8, 4))
print(arr)

print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])

print(arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])

