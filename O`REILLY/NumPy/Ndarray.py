
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



#Transposing Arrays and Swapping Axes

arr = np.arange(15).reshape((3, 5))

print(arr)
print(arr.T)


#X ^T X

arr = np.random.randn(6, 3)
print(np.dot(arr.T, arr))


arr = np.arange(16).reshape((2, 2, 4))
print(arr)

print(arr.transponse((1, 0, 2)))


print(arr)
print(arr.swapaxes(1, 2))



#Universal Functions: Fast Element-wise Array Functions

arr = np.arange(10)
print(np.sqrt(arr))
print(np.exp(arr))


#Max

x = randn(8)

y = randn(8)

print(x)
print(y)

print(np.maximum(x, y))


#divmod

arr = randn(7) * 5
print(np.modf(arr))





#####################

#Data Processing Using Arrays

points = np.arange(-5, 5, 0.01) #1000 equally spaced points

xs, ys = np.meshgrid(points, points)


import matplotlib.pyplot as plt

z = np.sqrt(xs ** 2 + ys ** 2)

print(z)

plt.imshow(z, cmap = plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()



#Expressing Conditional Logic as Array Operations

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])

cond = np.array([True, False, True, True, False])


result = [(x if c else y)
          for x, y ,c in zip(xarr, yarr, cond)]

print(result)

#2 Var

result = np.where(cond, xarr, yarr)
print(result)



#Positiv =2 negative = -2

arr = randn(4, 4)
print(arr)

print(np.where(arr > 0, 2,-2))

print(np.where(arr > 0, 2, arr))   #Set only positive values to 2




result = []
for i in range(n):

    if cond1[i] and cond2[i]:
        result.append(0)

    elif cond1[i]:
        result.append(1)

    elif cond2[i]:
        result.append(3)

    else:
        result.append(3)



#Simple way

print(np.where(cond1 & cond2 , 0,
               np.where(cond1, 1,
                        np.where(cond2, 2, 3))))




#Mathematical and Statical Methods


arr = np.random.randn(5, 4)

print(arr.mean())

print(np.mean(arr))

print(arr.sum())

print(arr.mean(axis = 1))
print(arr.sum(0))

print(arr.cumsum(0))
print(arr.cumprod(1))


#Methods for Boolean Arrays

arr = randn(100)
print((arr > 0).sum())  #Number of positive values


bools = np.array([False, False, True, False])

print(bools.any())

print(bools.all())



#Sorting

arr = randn(8)
print(arr)

arr.sort()
print(arr)


arr = randn(5, 3)

print(arr)

arr.sort(1)     #Sorted by axes
print(arr)



#Unique and Other Set Logic

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

print(np.unique(names))

ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))



# tests membership of the values True|False

values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))
#array([ True, False, False,True, True, False, True], dtype=bool)




#Sorting Arrays on Disk in Binary Format

arr = np.arange(10)
np.save('some_array', arr)


print(np.load('some_array.npy'))


np.savez('array_archive.npz', a = arr, b = arr)

arch = np.load('array_archive.npz')
print(arch['b'])



#Lin Alg

x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[5., 23.], [-1, 7], [8, 9]])


print(x, y)

print(x.dot(y))

print(np.dot(x, np.ones(3)))



from numpy.linalg import inv, qr

X = randn(5, 5)

mat = X.T.dot(X)

print(inv(mat))

print(mat.dot(inv(mat)))

q, r = qr(mat)
print(r)



#Random Number Generation

samples = np.random.normal(size = (4, 4))
print(samples)


#Example: Random Walks
import random
position = 0
walk = [position]
steps = 1000

for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)