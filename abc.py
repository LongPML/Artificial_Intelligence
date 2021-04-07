import numpy as np

a=np.array([[1,4], [0,3]])
b=np.array([3,3])
print(a, b, a-b, np.linalg.norm(a-b, ord = 0))