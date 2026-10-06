import numpy as np

arr = np.array([10, 20, 30, 40])

percentage = (arr / np.sum(arr)) * 100

print(percentage)