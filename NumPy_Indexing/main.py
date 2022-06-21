import numpy as np

a = np.arange(10) ** 2

# ambil elemen array
print(a[0])
print(a[7])
print(a[-1])

# slecing array adalah mengambil elemen array yang diinginkan
print(a[0:7])
print(a[5:])
print(a[:5])
    
# iterasi array adalah cara untuk mengakses setiap elemen array
for i in a:
    print("value ", i)
