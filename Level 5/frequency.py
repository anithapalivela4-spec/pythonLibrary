import numpy as np

arr = np.array([1, 2, 2, 3, 3, 3, 4])

values, counts = np.unique(arr, return_counts=True)

for value, count in zip(values, counts):
    print(value, ":", count)