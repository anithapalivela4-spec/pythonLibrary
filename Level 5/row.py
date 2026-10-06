import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [5, 10, 15]])

row_sums = np.sum(arr, axis=1)

index = np.argmax(row_sums)

print("Row:", index)
print("Sum:", row_sums[index])