# cara melakukan manipulasi dalam operasi matrix yang dilakukan dalam berbagai dimensi untuk mendapatkan data baru yang dikumpulkan dari data yang dioperasikan
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
# fungsi shape digunakan untuk mengethuai dimensi yang akan dioperasikan dalam manipulasi matrix
print(a.shape)

# penggunaan transpose matrix digunakan untuk mengubah manipulasi baris menjadi coloumn begitu sebaliknya (change position matrix)
print("\nTranpose")
# cara satu
print(a.transpose())
# cara dua
# print(np.transpose(a))
# cara tiga
# print(a.T)

# penggunaan flatten array yang merubah manipulasi posisi matrix menjadi vector
print("\nFlatten")
print(a.ravel())

# penggunaan reshape matrix dengan manipulasi dalam merubah dimensi dan posisi matrix sesuai dengan kebutuhan data yang diinginkan
print("nReshape")
print(a.reshape(3, 2))

# resize matrix merupakan sebuah cara untuk merubah komposisi manipulasi matrix secara permanen
print("\nResize")
a.resize(3, 2)
print(a)
