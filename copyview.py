import numpy as np

#Copy Vs View
np1 = np.arange(6)

#Create a View
np2 = np1.view()

np1[0] = 43

print(f"Original NP1: {np1}")
print(f"Original NP2 : {np2}")

print(f"Changed NP1: {np1}")
print(f"Changed NP2 : {np2}")

""" Summary:
A copy creates a separate object with its own data, so changes to the original don't affect the copy.
A view shares the same data as the original, so changes to the original are reflected in the view (and vice versa). """