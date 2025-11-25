import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Configurações da Simulação ---
N_PARTICULAS = 150       # Número de partículas
TAM_CAIXA = 10.0         # Tamanho do recipiente (quadrado)
DT = 0.05                # Passo de tempo da simulação
FRAMES = 300             # Total de quadros da animação
TAXA_AUMENTO_VEL = 1.005 # Fator de multiplicação da velocidade por quadro (aumenta a "temperatura")
FRAME_PARADA_AUMENTO = 200 # Quadro em que a pressão para de subir para não ficar caótico demais

# --- Inicialização do Estado ---
# Posições iniciais aleatórias dentro da caixa (X e Y)
pos = np.random.rand(N_PARTICULAS, 2) * TAM_CAIXA

# Velocidades iniciais aleatórias (distribuição normal centrada em 0)
# Começamos com velocidades baixas para representar baixa pressão inicial
vel = np.random.randn(N_PARTICULAS, 2) * 0.5

# --- Configuração do Matplotlib ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, TAM_CAIXA)
ax.set_ylim(0, TAM_CAIXA)

# Remove os eixos para focar na "caixa"
ax.set_xticks([])
ax.set_yticks([])

# Desenha as paredes da caixa com uma linha mais grossa
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)

# Cria o objeto de dispersão (scatter plot) que representará as partículas
# Usamos um colormap (cmap) para mostrar a energia visualmente depois
particulas = ax.scatter(pos[:, 0], pos[:, 1], s=30, c='blue', cmap='plasma', vmin=0, vmax=1)

# Textos informativos
titulo_texto = ax.set_title("Sistema Isotrópico: Pressão Baixa", fontsize=12, fontweight='bold')
info_texto = ax.text(0.5, -0.05, '', transform=ax.transAxes, ha='center', fontsize=10)

# Variável para calcular uma "pseudo-pressão" média (energia cinética média)
energia_media_inicial = np.mean(np.sum(vel**2, axis=1))

# --- Função de Atualização da Animação ---
def update(frame):
    global pos, vel
    
    # 1. Atualiza Posição (Física básica: Posição = Posição Anterior + Velocidade * tempo)
    pos += vel * DT
    
    # 2. Tratamento de Colisões com as Paredes (Isotropia)
    # Se bater nas paredes verticais (X < 0 ou X > TAM_CAIXA), inverte a velocidade X
    mask_x = (pos[:, 0] < 0) | (pos[:, 0] > TAM_CAIXA)
    vel[mask_x, 0] *= -1
    
    # Se bater nas paredes horizontais (Y < 0 ou Y > TAM_CAIXA), inverte a velocidade Y
    mask_y = (pos[:, 1] < 0) | (pos[:, 1] > TAM_CAIXA)
    vel[mask_y, 1] *= -1
    
    # Corrige posições que eventualmente tenham saído ligeiramente da caixa devido ao passo de tempo
    pos[:, 0] = np.clip(pos[:, 0], 0, TAM_CAIXA)
    pos[:, 1] = np.clip(pos[:, 1], 0, TAM_CAIXA)

    # 3. AUMENTO DA PRESSÃO (Aumentando a velocidade/temperatura)
    # Aumentamos a velocidade gradualmente até um certo ponto
    estado_pressao = ""
    if frame < FRAME_PARADA_AUMENTO:
        vel *= TAXA_AUMENTO_VEL
        estado_pressao = "AUMENTANDO (Aquecendo)"
        titulo_texto.set_text("Sistema Isotrópico: Pressão AUMENTANDO 🔥")
        titulo_texto.set_color("red")
        
        # Faz as paredes "vibrarem" levemente para indicar tensão (efeito visual)
        vibra = np.random.randn() * 0.05 * (frame/FRAME_PARADA_AUMENTO)
        ax.set_xlim(0 - vibra, TAM_CAIXA + vibra)
        ax.set_ylim(0 - vibra, TAM_CAIXA + vibra)

        elif frame == FRAME_PARADA_AUMENTO:
         titulo_texto.set_text("Sistema Isotrópico: Pressão Alta (Estabilizada)")
         titulo_texto.set_color("darkred")
         estado_pressao = "ALTA E ESTÁVEL"
         # Reseta as paredes
         ax.set_xlim(0, TAM_CAIXA)
         ax.set_ylim(0, TAM_CAIXA)
    else:
         estado_pressao = "ALTA E ESTÁVEL"

    # 4. Atualização Visual
    # Calcula a velocidade escalar ao quadrado (proporcional à energia cinética)
    velocidade_escalar_sq = np.sum(vel**2, axis=1)
    energia_atual = np.mean(velocidade_escalar_sq)
    
    # Normaliza para usar no colormap (para mudar de azul para vermelho/amarelo)
    # O fator de divisão 60 é um ajuste empírico para a escala de cores ficar bonita
    cores_normalizadas = np.clip(velocidade_escalar_sq / 60.0, 0, 1)
    
    particulas.set_offsets(pos)
    particulas.set_array(cores_normalizadas) # Atualiza as cores baseadas na velocidade

    # Atualiza o texto de informação
    fator_pressao = energia_atual / energia_media_inicial
    info_texto.set_text(f"Status da Pressão: {estado_pressao}\nFator de Pressão Relativa: {fator_pressao:.2f}x")
    
    return particulas, titulo_texto, info_texto

# --- Criação e Execução da Animação ---
# interval=30 significa 30ms entre cada quadro (aprox 33 fps)
ani = animation.FuncAnimation(fig, update, frames=FRAMES, interval=30, blit=False)

plt.tight_layout()
plt.show()