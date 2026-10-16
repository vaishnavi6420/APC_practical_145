
import numpy as np

# Create a random 3D array
arr = np.random.randint(1, 101, size=(3, 4, 5))

# Flatten the array
flat = arr.flatten()

print("Original 3D Array:")
print(arr)

print("\nFlattened Array:")
print(flat)

# Display elements greater than 50
print("\nElements Greater Than 50:")
print(flat[flat > 50])

# Display even numbers
print("\nEven Numbers:")
print(flat[flat % 2 == 0])

# Display elements less than the average
avg = np.mean(flat)
print("\nAverage:", avg)
print("Elements Less Than Average:")
print(flat[flat < avg])
