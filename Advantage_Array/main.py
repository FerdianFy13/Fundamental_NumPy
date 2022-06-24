# cara membuat array dengan efisien dengan menggunakan sebuah method atau function sendiri yang telah disediakan oleh package dari python, yaitu NumPy

import numpy as np

# membuat sebuah matrix dengan memberikan tipe data sesuai dengan kebutuhan yang diinginkan
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)

# membuat sebuah matrix dengan menggunakan sebuah function tersendiri dalam pembuatan sebuah matrix dengan memanfaatkan penggunaan object oriented programming
def kuadrat(row, column):
    return column ** 3


def jumlah(row, column):
    return column + row


b = np.fromfunction(kuadrat, (2, 10), dtype=int)
c = np.fromfunction(jumlah, (4, 5), dtype=int)

# membuat sebuah matrix dengan menggunakan iterasi atau iterable
iterasi = (x * 4 for x in range(5))

d = np.fromiter(iterasi, dtype=int)

# menggunakan sebuah multiple array dengan menggunakan berbagai macam tipe data dalam pembuatan sebuah matrix
dtipe = [("nama", "S255"), ("tinggi", int)]
data = [("ucup", 150), ("otong", 160), ("mario", 180)]
e = np.array(data, dtype=dtipe)

print(a)
print(b)
print(c)
print(d)
print(e)
print(e[0])
