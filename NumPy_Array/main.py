import numpy as np


# vector adalah array yang berisi data yang berupa satu dimensi
a = np.array([1, 2, 3, 4, 5])
b = [1, 2, 3, 4, 5]

# membuat vector dengan range
c = np.arange(1, 10, 2)

# membuat llin space adalah membuat vector dengan jumlah data yang diberikan
d = list(np.linspace(1, 10, 5))

# membuat array multidimensi atau metrix
e = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# membuat matrix dengan value null
f = np.zeros((3, 3))

# membuat matrix identitas
g = np.identity(3)  # cara membuat identitas
g = np.eye(5)  # cara membuat eye identitas

print(a)
print(b)
print(c)
print(d)
print(e + 5)
print(f)
print(g)
