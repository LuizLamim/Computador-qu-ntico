import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def eh_primo(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Configurações da simulação
limite_max = 100  # Até que número vamos contar
x_vals = []
y_pi = []         # Valores reais de pi(x)
y_approx = []     # Aproximação x / ln(x)

contagem_primos = 0

# Preparar os dados (pré-cálculo para performance)
for x in range(2, limite_max + 1):
    if eh_primo(x):
        contagem_primos += 1
    
    x_vals.append(x)
    y_pi.append(contagem_primos)
    # Aproximação x / ln(x)
    y_approx.append(x / np.log(x))

# Configuração do gráfico
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#1e1e1e') # Fundo escuro estilo "Dark Mode"
ax.set_facecolor('#1e1e1e')

# Estilização dos eixos
ax.set_xlim(0, limite_max)
ax.set_ylim(0, max(y_pi) + 5)
ax.set_xlabel('x (Inteiros)', color='white')
ax.set_ylabel('Contagem', color='white')
ax.set_title(r'Função de Contagem de Primos $\pi(x)$ vs $x/\ln(x)$', color='white', fontsize=14)
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.grid(color='gray', linestyle='--', linewidth=0.3, alpha=0.5)