
import numpy as np

marks = np.array([
    45, 67, 89, 76, 54, 92, 81, 73, 60, 85,
    49, 95, 70, 88, 62, 78, 91, 56, 84, 68
])

average = np.mean(marks)

print("Marks:", marks)
print("Class Average:", average)
print("Marks Above Average:", marks[marks > average])
