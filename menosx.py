import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y = -x

plt.figure(figsize=(8, 6)) 

plt.plot(x, y, label=r'$f(x) = -x$', color='blue', linewidth=2) 

plt.grid(True, linestyle='--', alpha=0.6)

plt.title('Gráfico da Função f(x) = -x', fontsize=16)
plt.xlabel('Eixo X', fontsize=12)
plt.ylabel('Eixo Y / f(x)', fontsize=12)

