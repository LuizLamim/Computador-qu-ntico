import numpy as np
import matplotlib.pyplot as plt

# Define a grade de pontos onde o campo vetorial será avaliado
x, y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))

# Define o campo vetorial F(x, y) = <P(x, y), Q(x, y)>
# Vamos criar um campo com um rotacional não nulo para visualização
# Exemplo: F(x, y) = <-y, x>
P = -y
Q = x

# Calcula as componentes do rotacional (em 2D, a componente z do rotacional)
# Rotacional (2D) = ∂Q/∂x - ∂P/∂y
# Para o nosso exemplo: ∂Q/∂x = ∂(x)/∂x = 1
#                      ∂P/∂y = ∂(-y)/∂y = -1
# Rotacional = 1 - (-1) = 2

# Para visualizar o rotacional, podemos usar um heatmap ou círculos
# com tamanho e cor representando a magnitude e direção do rotacional.
# Como o rotacional é constante (2) neste exemplo, vamos representá-lo
# com uma cor de fundo.

# Cria a figura e os subplots
fig, ax = plt.subplots()

# Plota o campo vetorial usando setas
ax.quiver(x, y, P, Q, color='blue', angles='xy', scale_units='xy', scale=1)

# Define a cor de fundo para indicar o rotacional (constante neste caso)
ax.imshow([[2, 2], [2, 2]], extent=[-2, 2, -2, 2], alpha=0.3, cmap='viridis')
# A função imshow exibe dados como uma imagem. Aqui, usamos uma matriz 2x2
# com o valor do rotacional para criar um fundo colorido.
# 'extent' define a extensão da imagem para corresponder ao nosso campo vetorial.
# 'alpha' define a transparência.
# 'cmap' escolhe um mapa de cores.

# Adiciona um título ao gráfico
ax.set_title('Campo Vetorial Rotacional: F = <-y, x>')

# Adiciona rótulos aos eixos
ax.set_xlabel('x')
ax.set_ylabel('y')

# Define os limites dos eixos
ax.set_xlim([-2.5, 2.5])
ax.set_ylim([-2.5, 2.5])

# Garante que a escala dos eixos seja a mesma
ax.set_aspect('equal', adjustable='box')

# Adiciona uma legenda (opcional, mas pode ser útil para o mapa de cores)
# Podemos adicionar uma barra de cores se o rotacional não fosse constante.
# fig.colorbar(im, ax=ax, label='Magnitude do Rotacional')

# Mostra o gráfico
plt.show()