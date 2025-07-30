import numpy as np

# 1-d array
# np1 = np.arange(10)
# for x in np1:
#     print(x)

# 2-d array
np2 = np.array([[1,2,3,4,5],[4,5,6,7,8]])
for x in np2:
    for y in x:
        print(y)

#use np.nditer()

np3 = np.array([[[1, 2, 4, 5], [1, 2, 4, 6]], [[4, 6, 3, 2], [3, 4, 10, 2]]])
for x in np.nditer(np3):
    print(x)
