import numpy as np

# Definindo duas matrizes
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Multiplicação de matrizes usando np.dot
C = np.dot(A, B)
print("Multiplicação de Matrizes usando np.dot:\n", C)

# Multiplicação de matrizes usando o operador @
D = A @ B
print("Multiplicação de Matrizes usando o operador @:\n", D)
