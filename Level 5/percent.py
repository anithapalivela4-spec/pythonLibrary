import numpy as np

arr = np.array([10, np.nan, 20, np.nan, 30, 40])

missing_count = np.isnan(arr).sum()

percentage = (missing_count / arr.size) * 100

print("Missing percentage:", percentage)


