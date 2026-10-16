
import numpy as np

arr = np.array([10, 25, 45, 55, 60, 35, 75, 80, 40, 90])

print("Original Array:")
print(arr)

# Replace elements greater than 50 with 0
arr[arr > 50] = 0

print("\nModified Array:")
print(arr)
