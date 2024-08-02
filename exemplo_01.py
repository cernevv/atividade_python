import numpy as np

# Criação de um array de dados
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Cálculo da média e do desvio padrão
mean = np.mean(data)
std_dev = np.std(data)

print(f"Média: {mean}, Desvio Padrão: {std_dev}")
