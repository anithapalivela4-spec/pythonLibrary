import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [5, 10, 15]])

column_avg = np.mean(arr, axis=0)

index = np.argmin(column_avg)

print("Column:", index)
print("Average:", column_avg[index])