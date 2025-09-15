import numpy as np
import matplotlib.pyplot as plt

# Gera valores de x de -2*pi a 2*pi com 1000 pontos para uma curva suave
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

y = np.abs(np.sin(x) * np.cos(x))

# Cria a figura e os eixos
plt.figure(figsize=(10, 6))

# Plota a função
plt.plot(x, y, label=r'$|sen(x)cos(x)|$')
