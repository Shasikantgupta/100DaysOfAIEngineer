# Broadcasting in NumPy refers to the ability of NumPy to perform operations on arrays of different shapes.
# When performing operations on arrays, NumPy automatically expands the smaller array to match the shape of the larger array, allowing for element-wise operations without the need for explicit replication of data.
import numpy as np

# array + scaler
a = np.array([[1, 2, 3], [4, 5, 6]])
x= 10
b= a + x
print (b)

# arrat + array
a= np.array([[1, 2, 3], [4, 5, 6]])
b= np.array([[1], [2]])
c= a + b
print (c)

a= np.array([[1, 2, 3], [4, 5, 6]])
b= np.array([1, 2, 3])
c= a + b
print (c)

a= np.array([[1, 2, 3], [4, 5, 6]])
b= np.array([[1, 2, 3], [4, 5, 6]])
c= a + b
print (c)

# array * scaler
a= np.array([[1, 2, 3], [4, 5, 6]])
x= 10   
c= a * x
print (c)