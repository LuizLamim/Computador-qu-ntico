import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animar_orbita_planetaria():
    """
    Cria uma animação de um planeta orbitando uma estrela.
    """
    # Parâmetros da órbita (simplificados para demonstração)
    a = 10.0  # Semieixo maior da órbita (distância média)
    e = 0.5   # Excentricidade da órbita (0 para circular, >0 para elíptica)
    periodo = 200 # Período orbital em "unidades de tempo" (frames)

    # Posição da estrela (no foco da elipse)
    estrela_x = -a * e
    estrela_y = 0

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')
    ax.set_xlim(-a - 2, a + 2)
    ax.set_ylim(-a - 2, a + 2)
    ax.set_xticks([])
    ax.set_yticks([])

    # Desenha a estrela
    estrela, = ax.plot(estrela_x, estrela_y, 'o', color='gold', markersize=20, label='Estrela')

    # Desenha o planeta
    planeta, = ax.plot([], [], 'o', color='blue', markersize=10, label='Planeta')

    # Desenha a trajetória da órbita (elipse)
    theta_orbita = np.linspace(0, 2 * np.pi, 1000)
    r_orbita = a * (1 - e**2) / (1 + e * np.cos(theta_orbita))
    x_orbita = r_orbita * np.cos(theta_orbita) + estrela_x
    y_orbita = r_orbita * np.sin(theta_orbita)
    ax.plot(x_orbita, y_orbita, 'k--', alpha=0.5, lw=1, label='Órbita')

    ax.legend(loc='upper right')
    plt.title('Animação de um Planeta Orbitando uma Estrela')

    # Função de inicialização
    def init():
        planeta.set_data([], [])
        return planeta,

    # Função de animação
    def animate(i):
        # Calcula o ângulo verdadeiro (anomalia verdadeira) para o tempo 'i'
        # Usando a anomalia excêntrica para uma órbita elíptica
        M = 2 * np.pi * i / periodo  # Anomalia Média

        # Equação de Kepler: M = E - e * sin(E)
        # Resolve E (Anomalia Excêntrica) iterativamente
        E = M
        for _ in range(10): # Iterações para convergência
            E = M + e * np.sin(E)

        # Calcula a anomalia verdadeira (theta)
        theta = 2 * np.arctan(np.sqrt((1 + e) / (1 - e)) * np.tan(E / 2))

        # Calcula a distância do planeta à estrela (raio)
        r = a * (1 - e * np.cos(E))

        # Posição do planeta em coordenadas cartesianas (relativo à estrela)
        x_planeta_relativo = r * np.cos(theta)
        y_planeta_relativo = r * np.sin(theta)

        # Posição absoluta do planeta
        x_planeta = x_planeta_relativo + estrela_x
        y_planeta = y_planeta_relativo

        planeta.set_data(x_planeta, y_planeta)
        return planeta,

    # Cria a animação
    ani = animation.FuncAnimation(fig, animate, frames=periodo,
                                  init_func=init, blit=True, interval=20)

    plt.show()

# Chama a função para rodar a animação
if __name__ == '__main__':
    animar_orbita_planetaria()