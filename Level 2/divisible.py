import numpy as np

arr = np.array([10, 12, 15, 20, 23, 25])

print(arr[arr % 5 == 0])