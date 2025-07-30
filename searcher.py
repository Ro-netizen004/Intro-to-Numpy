import numpy as np

#search

np1 = np.array([1,2,4,56,5,7,34,45,64,2,23,2,56])

x = np.where(np1 == 2)
print(x[0])

#return even items
y = np.where(np1%2==0)
print(y[0])