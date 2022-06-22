import numpy as np

a = np.array([1, 3, 5])
b = np.array([4, 6, 8])

# mengubah menjadi baris atau row
c = np.hstack([a, b])
# mengubah menjadi kolom atau column
c2 = np.vstack([a, b])
print(c)
print(c2)
