import numpy as np # type: ignore

# a) Create 5x5 array with random floats
arr = np.random.rand(5,5)

print("Original Array:")
print(arr)

# b) Save array to file
np.save("data.npy", arr)
print("\nArray saved to data.npy")

# c) Load array
loaded_arr = np.load("data.npy")

print("\nLoaded Array:")
print(loaded_arr)

# Verify dimensions
print("\nShape:", loaded_arr.shape)