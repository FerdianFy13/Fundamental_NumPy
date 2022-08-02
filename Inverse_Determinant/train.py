import numpy as np

a = np.array([[0, 1, 5], [3, -6, 9], [2, 6, 1]])
print(a)

a_inverse = np.linalg.inv(a)
print(a_inverse)

det_a = np.linalg.det(a)
print(det_a)