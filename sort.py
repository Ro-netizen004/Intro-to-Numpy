import numpy as np

#np.sort() numerical

np1 = np.array([1,2,3,4,5,6,7,0])
print(np.sort(np1))

#Alphabetical sorting
np2 = ["John","Xanther","Linda"]
print(np.sort(np2))

np3 = [True, False, False, True]
print(np.sort(np3))

# Returns a copy, does not change the original

# 2-d
np4 = np.array([[4,2,1],[45,1,20]])
print(np.sort(np4))