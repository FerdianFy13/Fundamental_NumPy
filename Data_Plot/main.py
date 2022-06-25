# penggabungan package NumPy dan Mathpolib dalam pembuatan data plot untuk menghasilkan sebuah data baru
import numpy as np
import matplotlib.pyplot as plt

# linear equation
# y = 2x + 3

x = np.arange(1, 10, 1)
y = 2 * x + 3
print(x)
print(y)

plt.figure(1)
plt.plot(x, y)
plt.show()

# circle
r = 10

corner = np.linspace(0, 2 * np.pi)
x2 = r * np.cos(corner)
y2 = r * np.sin(corner)

plt.figure(2)
plt.plot(x2, y2)
# untuk menampilkan dalam bentuk grafik dari fungdi plot menggunakan package matpolib
plt.show()
