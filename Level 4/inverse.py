import numpy as np

arr = np.array([[1, 2],
                [3, 4]])

inverse = np.linalg.inv(arr)

print(inverse)