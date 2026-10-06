import numpy as np

arr = np.array([-10, 20, -5, 30, -2])

arr[arr < 0] = 0

print(arr)