import numpy as np # type: ignore

# Create array (3,5)
arr = np.random.randint(1, 51, size=(3,5))

print("Array:")
print(arr)

# a) Mean and variance
print("\nMean:", np.mean(arr))
print("Variance:", np.var(arr))

# b) Min and max along each column
print("\nMinimum of each column:", np.min(arr, axis=0))
print("Maximum of each column:", np.max(arr, axis=0))

# c) Sum of each row
print("\nSum of each row:", np.sum(arr, axis=1))