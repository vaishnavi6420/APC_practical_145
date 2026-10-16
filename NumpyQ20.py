
import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("Sum of All Elements:", np.sum(arr))
print("Sum of Each Layer:", np.sum(arr, axis=(1, 2)))
print("Sum Along Rows:", np.sum(arr, axis=1))
print("Sum Along Columns:", np.sum(arr, axis=2))
