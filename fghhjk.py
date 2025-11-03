import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- 1. Configuração da Figura e Eixos ---
fig, ax = plt.subplots()

# Defina o intervalo para x e o valor base da exponencial (a > 1 para crescimento)
x = np.linspace(0, 5, 500)
base_exponencial = 1.5

# Calcula os valores de y para toda a curva (para configurar os limites do eixo y)
y_max = base_exponencial**5 

# Configura os limites dos eixos
ax.set_xlim(x.min(), x.max())
ax.set_ylim(0, y_max * 1.1) # Um pouco mais alto que o valor máximo
ax.grid(True)
ax.set_title(f'Animação da Curva Exponencial: y = {base_exponencial}^x')
ax.set_xlabel('x')
ax.set_ylabel('y')