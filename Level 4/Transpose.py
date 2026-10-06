import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Original shape:", arr.shape)

transpose = arr.T

print(transpose)
print("Transpose shape:", transpose.shape)