# melakukan sorting atau mengurutkan data array dari matrix yang dibuat pada package numpy dalam bahasa pemrograman python

import numpy as np

a = np.floor(np.random.randn(2, 2) * 10)

print(a)
print("Nilai maksimum dari matrix berikut adalah", a.max())
print("Posisi maksimum dari matrix berikut adalah", a.argmax())
print("Nilai minimum dari matrix berikut adalah", a.min())
print("Posisi minimum dari matrix berikut adalah", a.argmin())
print("urutan data adalah ", np.sort(a))
print("urutan data berdasarkan posisi value adalah ", np.argsort(a))
