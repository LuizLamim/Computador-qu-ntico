import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Configurações da Simulação ---
# A população dobra a cada unidade de tempo.
# N(t) = N0 * 2^t
N0 = 1  # População inicial
tempo_maximo = 10 # Vamos simular 10 ciclos de duplicação

# --- Preparar a figura e os eixos ---
fig, (ax_graph, ax_text) = plt.subplots(2, 1, figsize=(8, 8), gridspec_kw={'height_ratios': [3, 1]})
fig.suptitle('Crescimento Exponencial Bacteriano: N(t) = $1 \cdot 2^t$', fontsize=14)

# Configuração do Gráfico (Eixo superior)
t_vals = np.linspace(0, tempo_maximo, 200)
n_vals = N0 * (2**t_vals)

ax_graph.set_xlim(0, tempo_maximo)
ax_graph.set_ylim(0, N0 * (2**tempo_maximo))
ax_graph.set_xlabel('Tempo (t) - Ciclos de Divisão')
ax_graph.set_ylabel('População de Bactérias (N)')
ax_graph.grid(True, linestyle='--')

line, = ax_graph.plot([], [], 'g-', lw=3) # Linha verde para bactérias
point, = ax_graph.plot([], [], 'ro', markersize=8) # Ponto atual vermelho

# Configuração da Área de Texto (Eixo inferior)
ax_text.axis('off') # Esconder eixos
time_text = ax_text.text(0.1, 0.7, '', fontsize=16)
pop_text = ax_text.text(0.1, 0.4, '', fontsize=16, color='green', fontweight='bold')
note_text = ax_text.text(0.1, 0.1, '', fontsize=12, style='italic')

# --- Função de Inicialização da Animação ---
def init():
    line.set_data([], [])
    point.set_data([], [])
    time_text.set_text('')
    pop_text.set_text('')
    note_text.set_text('Iniciando com 1 bactéria...')
    return line, point, time_text, pop_text, note_text

# --- Função de Atualização (Frame a Frame) ---
def animate(i):
    # 'i' é o índice do frame. Vamos usar frames para representar o tempo.
    # Total de frames = 200.
    t_current = t_vals[i]
    n_current = N0 * (2**t_current)
    
    # Atualizar gráfico
    line.set_data(t_vals[:i], n_vals[:i])
    point.set_data([t_current], [n_current])
    
    # Atualizar textos
    time_text.set_text(f'Tempo decorrido: {t_current:.2f}')
    pop_text.set_text(f'População: {int(n_current):,} bactérias')
    
    # Notas dinâmicas baseadas no estágio do crescimento
    if t_current < 3:
        note = "Fase Inicial: Crescimento parece lento."
    elif t_current < 7:
        note = "Aceleração: A cada ciclo, o número de novas bactérias é maior."
    elif t_current < 9:
        note = "Crescimento Explosivo: A curva se torna íngreme."
    else:
        note = "Fase Final: O número dobra massivamente em pouco tempo!"
        
    note_text.set_text(note)

    return line, point, time_text, pop_text, note_text