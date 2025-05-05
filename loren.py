import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorenz(xyz, *, s=10, r=28, b=2.667):
    """
    Define as equações do Atractor de Lorenz.

    Parâmetros
    ----------
    xyz : array-like, shape (3,)
        Ponto de interesse no espaço tridimensional.
    s, r, b : float
        Parâmetros que definem o Atractor de Lorenz.

    Retorna
    -------
    xyz_dot : array, shape (3,)
        Valores das derivadas parciais do Atractor de Lorenz no ponto *xyz*.
    """
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])

# Configurar os parâmetros
dt = 0.01
num_steps = 10000

# Inicializar arrays para armazenar as coordenadas
xyzs = np.empty((num_steps + 1, 3))

# Definir as condições iniciais
xyzs[0] = (0., 1., 1.05)

# Simular o sistema de Lorenz
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt

# Plotar o Atractor de Lorenz em 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

ax.plot(xyzs[:, 0], xyzs[:, 1], xyzs[:, 2], lw=0.5)
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_zlabel("Eixo Z")
ax.set_title("Atractor de Lorenz")

plt.show()