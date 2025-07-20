import numpy as np
import matplotlib.pyplot as plt

def simular_orbita():
    """
    Simula a órbita da Terra em torno do Sol usando um método numérico simples.
    """

    # --- Constantes (ajustadas para simplificação) ---
    G = 1.0  # Constante gravitacional (simplificada)
    M_sol = 1.0  # Massa do Sol (simplificada)

    # --- Condições Iniciais da Terra ---
    # Posição inicial (em unidades arbitrárias)
    # A Terra começa no "eixo x" a uma distância de 1 unidade do Sol.
    posicao_x_inicial = 1.0
    posicao_y_inicial = 0.0

    # Velocidade inicial (para uma órbita aproximadamente circular/elíptica)
    # A velocidade tangencial necessária para uma órbita quase circular
    # é sqrt(G * M_sol / r), onde r é a distância inicial.
    velocidade_x_inicial = 0.0
    velocidade_y_inicial = np.sqrt(G * M_sol / posicao_x_inicial)

    # --- Parâmetros da Simulação ---
    tempo_total = 10 * 2 * np.pi  # Tempo total de simulação (equivalente a 10 "anos" orbitais)
    passo_tempo = 0.001           # Tamanho do passo de tempo

    # Número de passos na simulação
    num_passos = int(tempo_total / passo_tempo)

    # --- Armazenamento de Dados ---
    # Listas para armazenar as posições ao longo do tempo
    posicoes_x = []
    posicoes_y = []

    # --- Inicialização ---
    posicao_atual_x = posicao_x_inicial
    posicao_atual_y = posicao_y_inicial
    velocidade_atual_x = velocidade_x_inicial
    velocidade_atual_y = velocidade_y_inicial

    # --- Loop de Simulação ---
    print(f"Iniciando simulação com {num_passos} passos...")
    for _ in range(num_passos):
        # 1. Calcular a distância da Terra ao Sol
        distancia_ao_sol = np.sqrt(posicao_atual_x**2 + posicao_atual_y**2)

        # 2. Calcular a força gravitacional (módulo)
        # F = G * M_sol * m_terra / r^2.
        # Assumimos m_terra = 1 para simplificar, então F = G * M_sol / r^2
        forca_gravitacional_modulo = (G * M_sol) / (distancia_ao_sol**2)

        # 3. Calcular as componentes da força (vetorial)
        # As componentes da força apontam na direção do Sol.
        # Vetor unitário da Terra para o Sol: (-pos_x/dist, -pos_y/dist)
        forca_x = -forca_gravitacional_modulo * (posicao_atual_x / distancia_ao_sol)
        forca_y = -forca_gravitacional_modulo * (posicao_atual_y / distancia_ao_sol)

        # 4. Calcular as acelerações (a = F/m)
        # Assumimos m_terra = 1, então a = F
        aceleracao_x = forca_x
        aceleracao_y = forca_y

        # 5. Atualizar a velocidade (v_new = v_old + a * dt)
        velocidade_atual_x += aceleracao_x * passo_tempo
        velocidade_atual_y += aceleracao_y * passo_tempo

        # 6. Atualizar a posição (p_new = p_old + v_new * dt)
        posicao_atual_x += velocidade_atual_x * passo_tempo
        posicao_atual_y += velocidade_atual_y * passo_tempo

        # 7. Armazenar as posições
        posicoes_x.append(posicao_atual_x)
        posicoes_y.append(posicao_atual_y)

    print("Simulação concluída.")
    return posicoes_x, posicoes_y

def plotar_orbita(posicoes_x, posicoes_y):
    """
    Plota a órbita simulada da Terra e a posição do Sol.
    """
    plt.figure(figsize=(8, 8))
    plt.plot(posicoes_x, posicoes_y, label='Órbita da Terra', color='blue')
    plt.plot(0, 0, 'o', markersize=10, color='orange', label='Sol') # Sol na origem
    plt.title('Simulação da Órbita da Terra em torno do Sol')
    plt.xlabel('Posição X')
    plt.ylabel('Posição Y')
    plt.grid(True)
    plt.axis('equal') # Garante que os eixos tenham a mesma escala
    plt.legend()
    plt.show()

if __name__ == "__main__":
    x_orbit, y_orbit = simular_orbita()
    plotar_orbita(x_orbit, y_orbit)