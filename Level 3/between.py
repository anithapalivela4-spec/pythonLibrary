import numpy as np

arr = np.array([10, 20, 30, 50, 80, 90])

print(arr[(arr >= 20) & (arr <= 80)])