import numpy as np
import matplotlib.pyplot as plt

def plot_magnetic_field():
    # 1. Configurar a grade (o espaço onde o campo será calculado)
    # Criamos uma matriz de pontos X e Y variando de -2 a 2
    nx, ny = 100, 100
    x = np.linspace(-2, 2, nx)
    y = np.linspace(-2, 2, ny)
    X, Y = np.meshgrid(x, y)

    # 2. Definir o momento de dipolo magnético
    # m = (0, 1) significa que o polo norte aponta para cima (eixo Y)
    m_vector = np.array([0, 1])

    # 3. Calcular a distância e os vetores de posição
    # R é a distância da origem até cada ponto (x, y)
    R = np.sqrt(X**2 + Y**2)
    
    # Evitar divisão por zero na origem adicionando um valor minúsculo
    R[R == 0] = 1e-10

    # Produto escalar entre o momento de dipolo e o vetor posição (m . r)
    # Aqui, como m é (0,1), m.r é apenas Y. Mas faremos genericamente:
    dot_mr = m_vector[0] * X + m_vector[1] * Y
    
    # Constante física (simplificada para 1 para visualização)
    # A fórmula real seria (mu_0 / 4pi)
    constante = 1.0

    # 4. Calcular o vetor Campo Magnético (B) em cada ponto
    # Fórmula: B = (3 * (m . r) * r / r^5) - (m / r^3)
    
    # Componente vetorial (3 * (m . r) * r)
    vec_term_x = 3 * dot_mr * X
    vec_term_y = 3 * dot_mr * Y
    
    # Componentes finais Bx e By
    Bx = constante * (vec_term_x / R**5 - m_vector[0] / R**3)
    By = constante * (vec_term_y / R**5 - m_vector[1] / R**3)

    # 5. Visualização
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Adicionando cores baseadas na magnitude do campo (logarítmico para melhor visualização)
    magnitude = np.sqrt(Bx**2 + By**2)
    color = 2 * np.log(magnitude) # Escala logarítmica suaviza as cores

    # Usamos streamplot para desenhar as linhas de campo (linhas de fluxo)
    strm = ax.streamplot(X, Y, Bx, By, color=color, linewidth=1.5, cmap='inferno', density=1.5, arrowstyle='->', arrowsize=1.5)
    
    # Adicionar um círculo representando o ímã no centro
    circle = plt.Circle((0, 0), 0.1, color='gray', zorder=10)
    ax.add_artist(circle)
    ax.text(-0.05, -0.05, 'N', color='red', fontsize=12, fontweight='bold', zorder=11)
    ax.text(-0.05, -0.25, 'S', color='blue', fontsize=12, fontweight='bold', zorder=11)

    # Configurações finais do gráfico
    plt.title('Campo Magnético de um Dipolo (Ímã)', fontsize=16)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.colorbar(strm.lines, label='Intensidade do Campo (Escala Log)')
    plt.grid(True, alpha=0.3)
    
    plt.show()

if __name__ == "__main__":
    plot_magnetic_field()