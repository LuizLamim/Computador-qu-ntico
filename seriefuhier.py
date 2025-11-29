import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configurações iniciais
plt.style.use('dark_background') # Estilo visual escuro (opcional)
fig, ax = plt.subplots(figsize=(10, 6))

# Dados do eixo X (de 0 a 4pi para mostrar dois ciclos)
x = np.linspace(0, 4 * np.pi, 1000)

# Função para calcular a Série de Fourier de uma Onda Quadrada
# Fórmula: (4/pi) * somatório(sen(n*x)/n) para n ímpar
def fourier_square_wave(x, n_terms):
    y = np.zeros_like(x)
    # Loop para somar os harmônicos ímpares (1, 3, 5, 7...)
    for k in range(1, n_terms * 2, 2):
        y += np.sin(k * x) / k
    return (4 / np.pi) * y