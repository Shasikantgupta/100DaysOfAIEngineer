# Reshaping the array using reshape() and flatten() function 

import numpy as np

# 1D array to 2D array
arr_1d= np.array([3,5,6,2,8,9,7,5,6,4])
arr_2d= arr_1d.reshape((2,5))
print (arr_2d)

# flatten() function is used to convert any dimention array to one dimention array 
arr_2d= np.array(([3,5,6,2,8],[9,7,5,6,4]))
arr= arr_2d.flatten()
print (arr)