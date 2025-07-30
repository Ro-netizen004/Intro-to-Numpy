"PART 1 OF INTRODUCTION TO NUMPY"
import numpy as np

list1 = [1, 2, 3, 4, 5]
print(list1)

list2 = ["John Elder", 41, list1, True]

#numpy - Numeric Python, special type of array, everything has to be of the 
#same data type
#nd array = n - dimensional array

np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#print(np1.shape)

""" For a 1D array, .shape returns a single-element tuple (length,).

For a 2D array, it returns (rows, columns).

For higher dimensions, it returns a tuple with the size for each axis.

Example:
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Output: (2, 3) """

#Range
np2 = np.arange(20)
#print(np2)

#Step
np3 = np.arange(0, 10, 2)
#print(np3)

#Zeros
np4 = np.zeros(10)
#print(np4)

#Multi-dimensional arrays
np5 = np.zeros((2, 3))
print(np5)
print(np5.shape)

#arange method only creates single dimension arrays
#to create multi-dimensional arrays with arange, reshape method has to be used


#Full
np6 = np.full((3,2), 6)
print(np6)
print(np6.shape)

#Converting regular python array to numpy array
np7 = np.array(list1)
print(np7)

