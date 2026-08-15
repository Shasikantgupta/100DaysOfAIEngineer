# Indexing and slicing in 1D array

import numpy as np 

arr= np.array([20,3,23,45,75,8,56,97,57,44])
print (arr[0:3])
print (arr[0: ])
print (arr[0: :2])
# with negative indexing 
print(arr[-1])
print (arr[-1:-10:-1])
print (arr[-1: :-1])