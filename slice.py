import numpy as np

#slicing numpy arrays
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

#return from 3 to 6:
#print(np1[2:])

#return negative slices, from end to beginning
#print(np1[::-1])

#return negative slices, 3, 4 , 5, 6
#print(np1[-6:-2])

np2 = np.arange(10)
#print(np2)
#print(np2[::2])

#2-d arrays
np3 = np.array([[1,2,3,5],[4,3,5,2]])
#print(np3.shape) 
#shape is (2, 4) as expected

#access 4 from the array, two ways to do this
# print(np3[1][0])
# print(np3[1,0])

#get 2,3 from np3
print(np3[0:1, 1:3])
print(np3[0:2, 1:3])