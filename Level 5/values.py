import numpy as np

arr = np.array([10, 20, 30, 40, 50])

mean = np.mean(arr)

print(arr[arr > mean])