import numpy as np
P = np.array([3,1])
B = np.array([[3,2], [3,3]])
G = np.array([[1,1], [1,4]])

print(np.linalg.norm(B[0] - P, ord=1))