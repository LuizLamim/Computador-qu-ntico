import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

y = np.abs(-3 * x + 4)

plt.figure(figsize=(10, 6))

plt.plot(x, y, label=r'$f(x) = |-3x + 4|$', color='blue')

plt.title('Gráfico da Função Modular $f(x) = |-3x + 4|$', fontsize=16)
plt.xlabel('Eixo x', fontsize=12)
plt.ylabel('Eixo y', fontsize=12)

plt.grid(True, linestyle='--', alpha=0.7)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)