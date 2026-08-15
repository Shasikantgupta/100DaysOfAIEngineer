# aggregation using array

import numpy as np
arr = np.array (([3, 5, 7, 4, 7], [8, 4, 5, 9, 10]))

# sum of all elements in array
print (np.sum(arr))

# sum of all elements in each row 
print (np.sum(arr, axis=1))

#sum of all elements in each column
print (np.sum(arr, axis=0))

# mean of all elements in array 
print (np.mean(arr))

# meam of all elements in each row 
print (np.mean(arr, axis=1))
 
# min of all elements in array 
print (np.min(arr))

#min of all elements in each row 
print (np.min(arr, axis=1))

# max of all elemnent in array
print (np.max(arr))

# max of all elements in each row 
print (np.max(arr, axis=1))

# std of all the elements in array 
print (np.std(arr))

# std of all the elements in each row 
print (np.std(arr, axis=1))

