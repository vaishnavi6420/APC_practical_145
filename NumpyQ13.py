
import numpy as np

# Create an unsorted array
arr = np.array([45, 12, 78, 23, 56, 9, 34])

print("Original Array:")
print(arr)

# Sort in ascending order
print("\nAscending Order:")
print(np.sort(arr))

# Sort in descending order
print("\nDescending Order:")
print(np.sort(arr)[::-1])
