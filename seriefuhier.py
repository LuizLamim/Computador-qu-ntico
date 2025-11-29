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

# Linha que será atualizada na animação (a aproximação)
line, = ax.plot([], [], lw=2, color='cyan', label='Aproximação de Fourier')

# Linha de referência (a onda quadrada perfeita) para comparação
y_ideal = np.sign(np.sin(x))
ax.plot(x, y_ideal, color='white', alpha=0.3, linestyle='--', label='Onda Quadrada Ideal')

# Configuração dos eixos
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title('Convergência da Série de Fourier (Onda Quadrada)', fontsize=14)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.2)

# Função de inicialização da animação
def init():
    line.set_data([], [])
    return line,

# Função de atualização (chamada a cada frame)
def update(frame):
    # O frame representa o número de termos (harmônicos) adicionados
    # Vamos acelerar um pouco multiplicando o frame
    num_termos = frame + 1
    
    y = fourier_square_wave(x, num_termos)
    line.set_data(x, y)
    
    # Atualiza o título com o número atual de termos
    ax.set_title(f'Série de Fourier - Termos somados: {num_termos}', fontsize=14)
    return line,

# Criar a animação
# frames=50: vai somar até 50 termos
# interval=200: 200 milissegundos entre cada frame
anim = FuncAnimation(fig, update, init_func=init, frames=50, interval=200, blit=True)

plt.tight_layout()
plt.show()