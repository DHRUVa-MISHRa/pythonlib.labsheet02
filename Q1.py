import numpy as np # type: ignore

# a) Generate 1D array from 1 to 12
arr = np.arange(1, 13)
print("Original array:")
print(arr)

# b) Reshape into 3x4 and 4x3
arr_3x4 = arr.reshape(3, 4)
arr_4x3 = arr.reshape(4, 3)

print("\n3x4 matrix:")
print(arr_3x4)

print("\n4x3 matrix:")
print(arr_4x3)

# c) Find shape and size
print("\nShape of 3x4:", arr_3x4.shape)
print("Size of 3x4:", arr_3x4.size)

print("\nShape of 4x3:", arr_4x3.shape)
print("Size of 4x3:", arr_4x3.size)