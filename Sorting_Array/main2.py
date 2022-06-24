# penggunaan cara dua dalam mengurutkan sebuah array dalam packaage dari NumPy dalam bahasa pemrograman python

import numpy as np

dtipe = [("nama", "S10"), ("tinggi", int)]
data = [("ucup", 250), ("otong", 160), ("mario", 180)]

a = np.array(data, dtype=dtipe)
print(a)

print(np.sort(a, order="tinggi"))
print(np.sort(a, order="nama"))
