import numpy as np

# 1-d array
np1 = np.arange(8)
print(np1.shape)

# 2-d array
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np2.shape)

#reshape
np3 = np1.reshape(2,4)
print(np3)
print(np3.shape)

np4 = np1.reshape(2,2,2)
print(np4)
print(np4.shape)

#Flatten to 1-d
np5 = np4.reshape(-1)
print(np5)
print(np5.shape)