import numpy as np

arr = np.array([10, 50, 30, 80, 60, 90])

largest = np.partition(arr, -3)[-3:]

third_largest = np.min(largest)

print(third_largest)