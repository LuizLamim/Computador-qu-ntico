import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4 * np.pi, 4 * np.pi, 1000)

y = np.sin(x) + 10 * np.cos(x)

plt.figure(figsize=(10, 6)) # Define o tamanho da figura
plt.plot(x, y, label=r'$\sin(x) + 10\cos(x)$', color='blue')