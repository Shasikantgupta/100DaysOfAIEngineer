# Day 1 Notes — NumPy Basics

## What is NumPy?

NumPy is a Python library used for working with numbers, arrays, and mathematical operations.

The main data structure in NumPy is called an `ndarray`, which allows us to work with one-dimensional and multidimensional data efficiently.

## Why NumPy?

NumPy makes numerical calculations easier and faster than working with normal Python lists and loops.

It is also widely used in Data Science, Machine Learning, and Deep Learning because models work heavily with numerical data and arrays.

## What I Learned

Today I learned about:

* NumPy arrays (`ndarray`)
* Array creation
* `shape`, `ndim`, `dtype`, and `size`
* Indexing and slicing
* Arithmetic operations on arrays
* Aggregation functions like `sum()`, `mean()`, `min()`, `max()`, and `std()`
* Reshaping arrays
* Broadcasting
* Vectorization
* The `axis` parameter

## Broadcasting

Broadcasting allows NumPy to perform operations between arrays with compatible shapes without manually repeating the values.

For example, adding a single number to an entire array can be done directly without using a loop.

I found this useful because it makes array operations much simpler and cleaner.

## Vectorization

Vectorization means performing an operation on an entire array instead of processing each element using a Python loop.

For example, instead of looping through every number and multiplying it by 2, NumPy allows us to simply multiply the entire array by 2.

This makes the code shorter and can also make numerical operations much faster.

## What I Found Challenging

Understanding `axis=0` and `axis=1` was a little confusing at first.

I understood it better by practicing with small 2D arrays and checking the results for rows and columns.

## What I Need to Revise

* NumPy array shapes
* `axis=0` vs `axis=1`
* Broadcasting rules
* Reshaping multidimensional arrays
* Vectorization

## Key Takeaway

The biggest thing I learned today is that NumPy is not just about creating arrays. It provides an efficient way to perform operations on large amounts of numerical data without writing unnecessary loops.

These concepts will be important as I move into Machine Learning and Deep Learning.

**Day 1 completed. 🚀**
