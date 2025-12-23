import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import quad # Para calcular o valor real e mostrar na tela

# --- 1. Configuração Inicial ---

# A função matemática
def f(x):
    return x**2 + np.cos(x)

# Limites da integração
start_limit = 0
end_limit = 5

# Dados para o gráfico estático (fundo)
x_static = np.linspace(-1, 6, 500)
y_static = f(x_static)

# Configuração da Figura e Eixos
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-1, 6)
ax.set_ylim(-2, 30) # Fixar o Y para o gráfico não ficar pulando

# Desenhar elementos estáticos (que não mudam)
ax.plot(x_static, y_static, 'b-', linewidth=2, label=r'$f(x) = x^2 + \cos(x)$')
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title("Visualizando a Acumulação da Integral", fontsize=14)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend(loc='upper left')

# --- 2. Variáveis de Controle da Animação ---

# Esta variável vai guardar o objeto do preenchimento atual
# para podermos apagá-lo no próximo quadro.
current_fill = None
# Texto para mostrar o valor numérico crescente
valor_texto = ax.text(0.5, 25, '', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))


# --- 3. A Função de Atualização (O coração da animação) ---

def update(frame_x_limit):
    """
    Esta função é chamada repetidamente pelo FuncAnimation.
    'frame_x_limit' é o valor atual de X onde a animação está (ex: 0.1, 0.2, ..., 5.0)
    """
    global current_fill
    
    # A. Limpar o quadro anterior
    # Se já existe um preenchimento desenhado, nós o removemos.
    if current_fill:
        current_fill.remove()
    
    # B. Calcular a nova área para este quadro
    # Criamos pontos X que vão do início (0) até o limite atual deste quadro
    x_area = np.linspace(start_limit, frame_x_limit, 200)
    y_area = f(x_area)
    
    # C. Desenhar o novo preenchimento
    current_fill = ax.fill_between(x_area, y_area, color='skyblue', alpha=0.6)
    
    # D. (Opcional) Calcular e mostrar o valor numérico da integral até esse ponto
    current_integral_val, _ = quad(f, start_limit, frame_x_limit)
    valor_texto.set_text(f'Integral de {start_limit} até {frame_x_limit:.2f} = {current_integral_val:.4f}')
    
    # A função update deve retornar os objetos que foram modificados
    return current_fill, valor_texto

# --- 4. Criar a Animação ---

# Definir os quadros: vamos criar 100 passos entre 0.01 e 5
frames = np.linspace(start_limit + 0.01, end_limit, 100)

# FuncAnimation(figura, funcao_update, frames=lista_de_valores, interval=ms)
# interval=50 significa 50 milissegundos entre cada quadro
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=False, repeat=False)

plt.show()