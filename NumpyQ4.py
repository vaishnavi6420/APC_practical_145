
import numpy as np

# Create an array of integers from 1 to 20
arr = np.arange(1, 21)

# Separate even and odd numbers using Boolean indexing
even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

# Display the results
print("Original Array:", arr)
print("Even Numbers:", even)
print("Odd Numbers:", odd)
