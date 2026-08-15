# Array basics using numpy

import numpy as np

arr = np.array ([25, 26, 54, 5, 12, 60])
print (arr)
print (arr.ndim)
print (arr.shape)
print (arr.dtype)
print (arr.size)


## Creating np array using np function 
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


## arithmatic operations

import numpy as np
a = np.array ([5, 6, 0, 3,2])
b = np.array ([1, 2, 4, 6,2])

c = a + b
print (c)

c = a - b
print (c)

c = a*b
print (c)

c = a**b
print (c)

c = a/b
print (c)


## aggregation using array

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



## Indexing and slicing in 1D array

import numpy as np 

arr= np.array([20,3,23,45,75,8,56,97,57,44])
print (arr[0:3])
print (arr[0: ])
print (arr[0: :2])
# with negative indexing 
print(arr[-1])
print (arr[-1:-10:-1])
print (arr[-1: :-1])



## Reshaping the array using reshape() and flatten() function 

import numpy as np

# 1D array to 2D array
arr_1d= np.array([3,5,6,2,8,9,7,5,6,4])
arr_2d= arr_1d.reshape((2,5))
print (arr_2d)

# flatten() function is used to convert any dimention array to one dimention array 
arr_2d= np.array(([3,5,6,2,8],[9,7,5,6,4]))
arr= arr_2d.flatten()
print (arr)



## Broadcasting in NumPy refers to the ability of NumPy to perform operations on arrays of different shapes.
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



#import numpy as np

# ---- ARRAYS (1) ----
marks = np.array([
    [85, 78, 92, 88],
    [72, 69, 75, 80],
    [90, 95, 89, 94],
    [60, 65, 70, 68],
    [88, 84, 91, 87]
])

# ---- SHAPE (1) ----
n_students, n_subjects = marks.shape
print(f"Shape: {marks.shape} -> {n_students} students, {n_subjects} subjects\n")

# ---- INDEXING (1): get a single student's row ----
print("First student's marks:", marks[0])

# ---- SLICING (1): get all marks for the first subject (all rows, column 0) ----
print("All marks in Subject 1:", marks[:, 0], "\n")

# ---- AXIS + AGGREGATION (1): per-student stats -> axis=1 (across each row) ----
student_avg = marks.mean(axis=1)
student_high = marks.max(axis=1)
student_low = marks.min(axis=1)
student_std = marks.std(axis=1)

# ---- AXIS + AGGREGATION (2): per-subject stats -> axis=0 (across each column) ----
subject_avg = marks.mean(axis=0)
subject_high = marks.max(axis=0)
subject_low = marks.min(axis=0)

# Class average = aggregation with no axis (whole matrix)
class_avg = marks.mean()

print("Student averages:", student_avg)
print("Student highest:", student_high)
print("Student lowest:", student_low)
print("Student std dev:", student_std, "\n")

print("Subject averages:", subject_avg)
print("Subject highest:", subject_high)
print("Subject lowest:", subject_low, "\n")

print(f"Class average: {class_avg:.2f}")

# ---- BROADCASTING (1): compare array of averages to a single scalar ----
above_avg_mask = student_avg > class_avg
print("Above class average?:", above_avg_mask)

# ---- BROADCASTING (2): subtract scalar class average from every mark at once ----
diff_from_class_avg = marks - class_avg

# ---- VECTORIZATION (1): pass/fail for every student, no loop ----
pass_fail = np.where(student_avg >= 40, "Pass", "Fail")
print("Pass/Fail:", pass_fail)

# ---- VECTORIZATION (2): find the top student without a loop ----
top_student_index = np.argmax(student_avg)
print(f"\nTop student: Student {top_student_index + 1} "
      f"(avg = {student_avg[top_student_index]:.2f})")

print(f"Students above class average: {above_avg_mask.sum()}")