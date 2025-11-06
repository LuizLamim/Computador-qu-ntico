import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# --- 1. Configurações Físicas/Geométricas ---

# Altura máxima da simulação (em metros, aprox.)
ALTURA_MAX = 100
# Número de segmentos para modelar a curva do raio de luz
NUM_SEGMENTOS = 50
# Posição do objeto distante (a fonte da luz)
X_OBJETO = 1000  # Distância (metros)
Y_OBJETO = 50    # Altura (metros)

# --- 2. Simulação da Curvatura da Luz (Refração) ---

def indice_refracao(y):
    """
    Simula o índice de refração (n) em função da altura (y).
    
    No caso da Fata Morgana (miragem superior):
    - Camada de ar frio (inferior): n é mais alto.
    - Camada de ar quente (superior): n é mais baixo.
    
    Abaixo, simulamos uma inversão térmica: n decresce rapidamente no topo,
    depois se estabiliza.
    """
    # Valor base do índice de refração
    n_base = 1.00029
    # Um termo que simula a inversão térmica (n alto em y baixo)
    n_variacao = 0.00005 * np.exp(-y / 20)
    return n_base + n_variacao

def calcular_trajetoria_curva(x_obj, y_obj, num_seg):
    """
    Calcula uma trajetória curva (simplificada) devido à refração.
    A luz se curva em direção ao índice de refração mais alto (o ar frio).
    """
    x_coords = np.linspace(0, x_obj, num_seg)
    y_coords = np.zeros(num_seg)
    
    # Altura inicial (onde a luz "deixa" o objeto)
    y_coords[-1] = y_obj

    # Curvatura simulada: A luz se curva para baixo (em direção ao chão)
    # A curvatura é mais acentuada quando a variação de n é maior (próximo ao chão)
    for i in range(num_seg - 2, -1, -1):
        # Gradiente simplificado de curvatura baseado na altura
        curvatura = (indice_refracao(y_coords[i+1]) - indice_refracao(y_coords[i+1] - 1)) * 500000
        
        # O próximo ponto é ligeiramente mais baixo (curvando para baixo)
        y_coords[i] = y_coords[i+1] - (x_obj / num_seg) * curvatura
        
        # Garante que o raio não vá abaixo do "solo"
        if y_coords[i] < 0:
            y_coords[i] = 0
            break
            
    # O observador está na posição (0, y_coords[0]) e vê a imagem aparente
    return x_coords, y_coords

# --- 3. Configuração da Animação Matplotlib ---

# Inicializa a figura e o eixo
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, X_OBJETO + 100)
ax.set_ylim(-5, ALTURA_MAX)
ax.set_xlabel("Distância (m)")
ax.set_ylabel("Altura (m)")
ax.set_title("Simulação Geométrica de Fata Morgana (Refração)")
ax.grid(True)

# Desenha o solo
ax.hlines(0, 0, X_OBJETO + 100, color='gray', linestyle='-', linewidth=4, label='Solo (Ar Frio)')

# Desenha o objeto real (um ponto na distância)
obj_real, = ax.plot(X_OBJETO, Y_OBJETO, 'o', color='red', markersize=8, label='Objeto Real')

# Desenha a trajetória da luz (inicialmente vazia)
trajetoria, = ax.plot([], [], '-', color='orange', linewidth=2, label='Trajetória Curva da Luz')

# Desenha a linha de visão aparente (como o observador "pensa" que a luz viajou)
linha_aparente, = ax.plot([], [], '--', color='blue', linewidth=1, label='Linha de Visão Aparente')

# Posição do observador (próximo à origem, a uma altura baixa)
OBS_X = 0
OBS_Y = 5
observador, = ax.plot(OBS_X, OBS_Y, 's', color='black', markersize=8, label='Observador')

# Desenha a imagem aparente (onde o objeto *parece* estar)
img_aparente, = ax.plot([], [], 'x', color='blue', markersize=10, label='Imagem Aparente (Miragem)')

# Adiciona uma legenda para a estratificação (inversão térmica)
ax.text(X_OBJETO / 2, ALTURA_MAX * 0.9, 'Camada de Ar Quente (n Baixo)', color='red', ha='center')
ax.text(X_OBJETO / 2, ALTURA_MAX * 0.1, 'Camada de Ar Frio (n Alto)', color='blue', ha='center')

# --- 4. Função de Animação ---

# Frame 0: Inicialização (Apenas o setup)
def init():
    trajetoria.set_data([], [])
    linha_aparente.set_data([], [])
    img_aparente.set_data([], [])
    return trajetoria, linha_aparente, img_aparente

# Função de atualização (Não precisamos de animação quadro a quadro, 
# apenas mostrar o estado final da luz curvada)
def animate(frame):
    # A animação é estática, focada na explicação geométrica
    
    # 1. Trajetória REAL (Curvada)
    x_real, y_real = calcular_trajetoria_curva(X_OBJETO, Y_OBJETO, NUM_SEGMENTOS)
    trajetoria.set_data(x_real, y_real)
    
    # 2. Imagem Aparente
    
    # O observador vê a luz chegando em (OBS_X, OBS_Y) com um certo ângulo.
    # Ângulo = inclinação do último segmento do raio antes de chegar ao observador.
    
    # A luz chega no observador em (x_real[0], y_real[0]). O observador está em (OBS_X, OBS_Y)
    # Usamos os dois pontos mais próximos para calcular a tangente:
    x_chegada = x_real[1]
    y_chegada = y_real[1]
    
    # Calcula a inclinação (m) do raio ao chegar ao observador
    if (x_chegada - OBS_X) != 0:
        inclinacao = (y_chegada - OBS_Y) / (x_chegada - OBS_X)
    else:
        inclinacao = 0 # Evita divisão por zero
        
    # Ponto de Interceptação da linha reta aparente
    # A luz parece vir de onde esta linha reta (tangente) se origina
    # Equação da reta: y - y1 = m(x - x1)
    
    # O ponto onde a linha aparente atinge a distância do objeto real (X_OBJETO)
    y_aparente_na_distancia = OBS_Y + inclinacao * (X_OBJETO - OBS_X)
    
    # 3. Linha de Visão Aparente (Reta Tangente)
    x_aparente_line = np.array([OBS_X, X_OBJETO])
    y_aparente_line = np.array([OBS_Y, y_aparente_na_distancia])
    linha_aparente.set_data(x_aparente_line, y_aparente_line)
    
    # 4. Posição da Imagem Aparente
    img_aparente.set_data(X_OBJETO, y_aparente_na_distancia)
    
    # Texto Explicativo (Mostra que o objeto parece estar mais alto)
    ax.text(X_OBJETO + 50, Y_OBJETO, f'Real: {Y_OBJETO:.1f} m', color='red')
    ax.text(X_OBJETO + 50, y_aparente_na_distancia, f'Aparente: {y_aparente_na_distancia:.1f} m', color='blue')
    
    # O frame é fixo, mas a função 'animate' executa o cálculo
    return trajetoria, linha_aparente, img_aparente

# Cria a animação (usando interval=1 para que o cálculo estático seja executado)
ani = FuncAnimation(fig, animate, frames=1, init_func=init, blit=False, interval=1)

# Adiciona a legenda
ax.legend(loc='lower left')

plt.show()