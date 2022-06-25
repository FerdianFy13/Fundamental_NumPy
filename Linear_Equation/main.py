# menyelesaikan permasalahan linear dengan menggunakan methode linear aljabar yang telah disediakan oleh package NumPy dalam bahasa pemrograman python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([23, 14])

print(a)

# penggunaan linear aljabar dengan method solve untuk melakukan persamaaan linear dengan cara cepat
equation = np.linalg.solve(a, b)
print(equation)

# penggunaan inverse dengan perkalian dot matrix dengan cara biasa
a_inv = np.linalg.inv(a)
x = np.dot(a_inv, b)
print(x)
