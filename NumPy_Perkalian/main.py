# perkalian matrix
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.ones([2, 2])

# penggunaan cara satu
c = np.dot(a, b)

# penggunaan cara dua
c2 = a.dot(b)

# print(a)
# print(b)
# print(c)
print(c2)
