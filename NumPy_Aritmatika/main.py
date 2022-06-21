import numpy as np

# list of lists python
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

# array numpy
anp = np.array([1, 2, 3, 4, 5])
bnp = np.array([6, 7, 8, 9, 10])

# element wise operation adalah operasi yang dilakukan pada setiap elemen array
resultnp = anp + bnp
resultnp = anp - bnp
resultnp = anp * bnp
resultnp = anp / bnp

result = a + b

print(result)
print(resultnp)
