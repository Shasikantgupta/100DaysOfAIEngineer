# Creating np array using np function 
import numpy as np

# Array filled with zeros
arr_zeros = np.zeros(5)
print (arr_zeros) 

# 2D array filled with zeros
arr_zeros_2d =np.zeros((4,5))
print (arr_zeros_2d)

# array filled with ones 
arr_ones = np.ones(5)
print (arr_ones)

# 2d array filled with ones
arr_ones_2d = np.ones((4,6))
print (arr_ones_2d)

# array using linespace function 
arr_l = np.linspace(0,30,num=6)
print(arr_l)

# array using arange function 
arr_2= np.arange(0,30,6)
print (arr_2)

# Array reshaping using reshape() 
arr_3= np.array([3,4,6,7,9,5,3,85,23,44])
a= arr_3.reshape((5,2))
print(a)