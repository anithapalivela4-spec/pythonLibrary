import numpy as np

arr = np.arange(1, 13).reshape(4, 3)

parts = np.vsplit(arr, 2)

print(parts)