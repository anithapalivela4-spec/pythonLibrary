import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 8])

count = np.sum(arr % 2 == 0)
print(count)