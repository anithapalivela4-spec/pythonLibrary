import numpy as np

arr = np.arange(1, 13).reshape(3, 4)

parts = np.hsplit(arr, 2)

print(parts)