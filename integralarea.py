import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x):
    return -x**2 + 10*x - 10 

x_min = 1
x_max = 9

# Pontos para plotar a curva suavemente
x_curve = np.linspace(x_min - 1, x_max + 1, 400) 
y_curve = f(x_curve)

# 2. Configuração inicial da figura e do eixo
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_curve, y_curve, color='blue', linewidth=2, label=r'$f(x) = -x^2 + 10x - 10$')
ax.fill_between(x_curve, y_curve, color='lightblue', alpha=0.3, label='Área real (aprox.)') # Área real para comparação
ax.set_title('Aproximação da Área sob a Curva (Integração)')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xlim(x_min - 1.5, x_max + 1.5)
ax.set_ylim(min(y_curve) - 5, max(y_curve) + 5)
ax.legend()

# Linha vertical para os limites da integração
ax.axvline(x=x_min, color='gray', linestyle='--', alpha=0.7)
ax.axvline(x=x_max, color='gray', linestyle='--', alpha=0.7)

# Texto para exibir o número de retângulos e a área aproximada
rect_text = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12, verticalalignment='top')
area_text = ax.text(0.05, 0.90, '', transform=ax.transAxes, fontsize=12, verticalalignment='top')

# 3. Função de inicialização para a animação
# Esta função é chamada uma vez no início da animação
def init():
    return []

# 4. Função de atualização para cada frame da animação
# Ela recalcula e redesenha os retângulos a cada passo
def update(frame):
    ax.patches.clear() # Limpa os retângulos anteriores

    # O número de retângulos aumenta progressivamente
    num_rectangles = int(np.power(1.5, frame)) + 5 # Crescimento exponencial para visualização
    if num_rectangles > 200: # Limita o número máximo de retângulos
        num_rectangles = 200

    # Largura de cada retângulo
    dx = (x_max - x_min) / num_rectangles

    # Calcula a soma das áreas dos retângulos
    approx_area = 0

    # Desenha cada retângulo
    for i in range(num_rectangles):
        # Posição x do lado esquerdo do retângulo
        x_rect = x_min + i * dx
        # Altura do retângulo (usando o valor da função no ponto médio para melhor aproximação)
        # Ou podemos usar o lado esquerdo: height = f(x_rect)
        # Ou o lado direito: height = f(x_rect + dx)
        # Vamos usar o lado esquerdo para simplificar a visualização inicial
        height = f(x_rect)

        # Adiciona o retângulo ao eixo
        rect = plt.Rectangle((x_rect, 0), dx, height, edgecolor='red', facecolor='salmon', alpha=0.6)
        ax.add_patch(rect)

        # Soma a área deste retângulo
        approx_area += height * dx

    # Atualiza o texto na tela
    rect_text.set_text(f'Retângulos: {num_rectangles}')
    area_text.set_text(f'Área Aprox.: {approx_area:.2f}')

    return ax.patches + [rect_text, area_text]

# 5. Criar a animação
# `frames` define o número de passos da animação
# `interval` é o atraso entre os frames em milissegundos
# `blit=True` otimiza a renderização, redesenhando apenas o que mudou
ani = FuncAnimation(fig, update, frames=np.arange(1, 60), init_func=init, blit=True, interval=100)


plt.show()