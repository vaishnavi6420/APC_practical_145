
import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Original Matrix:")
print(arr)

print("\nSum of Each Row:")
print(np.sum(arr, axis=1))

print("\nSum of Each Column:")
print(np.sum(arr, axis=0))
