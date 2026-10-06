import numpy as np

A = np.array([[2, 1],
              [1, 3]])

B = np.array([5, 6])

solution = np.linalg.solve(A, B)

print("x =", solution[0])
print("y =", solution[1])