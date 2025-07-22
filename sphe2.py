import numpy as np
from mayavi import mlab

# Define a função implícita para a superfície
# A superfície é definida onde f(x, y, z) = 0
def f(x, y, z):
    return x**3 + 3*y**3 + 3*z**3 - 1

# Define o domínio para a visualização
# Ajuste esses valores para ver a parte da superfície que te interessa
xmin, xmax = -1.5, 1.5
ymin, ymax = -1.5, 1.5
zmin, zmax = -1.5, 1.5

# Cria uma grade de pontos
# O número de pontos determina a resolução da superfície
# Mais pontos = melhor resolução, mas mais lento
N = 100
x, y, z = np.ogrid[xmin:xmax:N*1j, ymin:ymax:N*1j, zmin:zmax:N*1j]

# Calcula os valores da função na grade
scalars = f(x, y, z)

# Plota a superfície usando o algoritmo Marching Cubes
# O valor 0.0 indica que estamos plotando onde f(x, y, z) = 0
mlab.contour3d(scalars, contours=[0.0], opacity=0.5, colormap='viridis')

# Adiciona eixos e título
mlab.axes()
mlab.title('$x^3 + 3y^3 + 3z^3 = 1$', size=0.5)

# Mostra a visualização
mlab.show()