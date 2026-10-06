import numpy as np

arr = np.array([10, 50, 20, 80, 30, 90])

indexes = np.argsort(arr)[-3:][::-1]

print("Indexes:", indexes)
print("Values:", arr[indexes])