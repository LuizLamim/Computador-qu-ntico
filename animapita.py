import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def pitagoras_animacao():
    """
    Cria uma animação do Teorema de Pitágoras.
    """
    a = 3  # Cateto a
    b = 4  # Cateto b
    c = np.sqrt(a**2 + b**2)  # Hipotenusa

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.set_xlim(-1, max(a, b, c) + 1)
    ax.set_ylim(-1, max(a, b, c) + 1)
    ax.set_xticks([])
    ax.set_yticks([])

    # Desenha o triângulo original
    triangulo, = ax.plot([], [], 'k-', lw=2)
    ax.text(a/2, 0, f'a={a}', ha='center', va='top')
    ax.text(0, b/2, f'b={b}', ha='right', va='center')
    ax.text(a/2, b/2, f'c={c:.2f}', ha='center', va='bottom', rotation=np.degrees(np.arctan2(-b, a)))


    # Quadrados iniciais
    quadrado_a, = ax.plot([], [], 'b-', lw=2)  # Azul para o quadrado de 'a'
    quadrado_b, = ax.plot([], [], 'r-', lw=2)  # Vermelho para o quadrado de 'b'
    quadrado_c, = ax.plot([], [], 'g-', lw=2)  # Verde para o quadrado de 'c' (hipotenusa)

    # Função de inicialização
    def init():
        triangulo.set_data([0, a, 0, 0], [0, 0, b, 0])
        quadrado_a.set_data([], [])
        quadrado_b.set_data([], [])
        quadrado_c.set_data([], [])
        return triangulo, quadrado_a, quadrado_b, quadrado_c

    # Função de animação
    def animate(i):
        # Quadrado do cateto 'a'
        if i <= 50:
            x_a = [0, a, a, 0, 0]
            y_a = [0, 0, a, a, 0]
            quadrado_a.set_data(x_a, y_a)
        else:
            quadrado_a.set_data([], []) # Esconde depois de um tempo

        # Quadrado do cateto 'b'
        if i <= 50:
            x_b = [0, -b, -b, 0, 0]
            y_b = [0, 0, b, b, 0]
            quadrado_b.set_data(x_b, y_b)
        else:
            quadrado_b.set_data([], []) # Esconde depois de um tempo

        # Transição para o quadrado da hipotenusa
        if i > 50:
            # Posição base do quadrado 'c'
            x_c_base = [a, 0, -b, a-b, a]
            y_c_base = [0, b, b+a, a, 0]

            # Fator de interpolação para mover os quadrados
            t = (i - 50) / 100.0  # de 0 a 1 em 100 frames

            # Simplesmente exibindo o quadrado de C no final
            quadrado_c.set_data(x_c_base, y_c_base)

            # Para uma animação mais complexa de "preenchimento", você precisaria
            # dividir os quadrados A e B em partes e movê-los individualmente
            # para dentro do quadrado C. Isso é significativamente mais complexo
            # do que o escopo desta resposta inicial.

            # Adiciona os quadrados de 'a' e 'b' movendo para o quadrado de 'c' (conceitual)
            # Esta parte é mais ilustrativa, não uma "movimentação" física real complexa
            # para preencher C de forma animada sem um algoritmo mais sofisticado.
            # Aqui estamos apenas mostrando os quadrados A e B sumindo e o C aparecendo.
            # Para uma demonstração real de preenchimento, precisaríamos de transformações e divisões.

            pass # O quadrado 'c' aparece na posição correta


        return triangulo, quadrado_a, quadrado_b, quadrado_c

    # Cria a animação
    # frames: número de quadros na animação
    # interval: tempo entre os quadros em ms
    # blit=True: otimização para redesenhar apenas o que mudou
    ani = animation.FuncAnimation(fig, animate, frames=150,
                                  init_func=init, blit=True, interval=50)

    plt.title('Animação do Teorema de Pitágoras')
    plt.show()

# Chama a função para rodar a animação
if __name__ == '__main__':
    pitagoras_animacao()