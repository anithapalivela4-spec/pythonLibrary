import numpy as np

arr = np.array([10, 30, 20, 30, 50, 40, 50])

unique_values = np.unique(arr)

second_largest = unique_values[-2]

print(second_largest)