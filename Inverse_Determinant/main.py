# inverse matrix adalah sebuah kebalikan dari nilai matrix misalnya x = 5 akan menjadi x^-1 = 1/ 5

import numpy as np

a = np.array([[-8, -6], [7, 5]])
print(a)

# untuk melakukan sebuah inverse dalam python menggunakan algoritma lineaj aljabar seperti matematika pada umumnya
a_inverse = np.linalg.inv(a)
print(a_inverse)

# determinant adalah sebuah value dari variable matrix yang akan dijalankan
det_a = np.linalg.det(a)
det_i = np.linalg.det(a_inverse)
print(det_i)
print(det_a)
