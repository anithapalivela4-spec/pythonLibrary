import numpy as np

arr = np.array([10, 20, np.nan, 30, np.nan, 40])

mean = np.nanmean(arr)

arr[np.isnan(arr)] = mean

print(arr)