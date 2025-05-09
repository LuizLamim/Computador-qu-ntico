import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Define as constantes do sistema
g = 9.8  # Aceleração devido à gravidade (m/s^2)
L1 = 1.0  # Comprimento do primeiro pêndulo (m)
L2 = 1.0  # Comprimento do segundo pêndulo (m)
m1 = 1.0  # Massa do primeiro pêndulo (kg)
m2 = 1.0  # Massa do segundo pêndulo (kg)

# 2. Define as equações diferenciais do movimento do pêndulo duplo
def equations_of_motion(t, y):
    theta1, z1, theta2, z2 = y

    c1 = np.cos(theta1)
    s1 = np.sin(theta1)
    c2 = np.cos(theta2)
    s2 = np.sin(theta2)
    c12 = np.cos(theta1 - theta2)
    s12 = np.sin(theta1 - theta2)

    theta1_dot = z1
    theta2_dot = z2

    z1_dot = (m2*L1*z1**2*s12 + m2*g*np.sin(theta2)*c12 - (m1+m2)*g*np.sin(theta1) - m2*L2*z2**2*s12) / (L1*(m1 + m2*s12**2))
    z2_dot = (-m2*L2*z2**2*s12*c12 + (m1+m2)*g*np.sin(theta1)*c12 - (m1+m2)*L1*z1**2*s12 - (m1+m2)*g*np.sin(theta2)) / (L2*(m1 + m2*s12**2))

    return theta1_dot, z1_dot, theta2_dot, z2_dot

# 3. Define as condições iniciais
theta1_0 = np.pi/2      # Ângulo inicial do primeiro pêndulo (radianos)
z1_0 = 0.0             # Velocidade angular inicial do primeiro pêndulo (radianos/s)
theta2_0 = np.pi/2 + 0.1 # Ângulo inicial do segundo pêndulo (radianos) - uma pequena perturbação para visualização interessante
z2_0 = 0.0             # Velocidade angular inicial do segundo pêndulo (radianos/s)
initial_conditions = [theta1_0, z1_0, theta2_0, z2_0]

# 4. Define o tempo de simulação
t_span = (0, 20)       # Intervalo de tempo da simulação (segundos)
t_eval = np.linspace(t_span[0], t_span[1], 500) # Pontos de tempo para avaliar a solução

# 5. Resolve as equações diferenciais
sol = solve_ivp(equations_of_motion, t_span, initial_conditions, t_eval=t_eval, method='DOP853')

# 6. Extrai os ângulos e velocidades angulares da solução
theta1 = sol.y[0]
theta2 = sol.y[2]

# 7. Calcula as coordenadas cartesianas dos pêndulos
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# 8. Cria a animação do pêndulo duplo
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-(L1 + L2 + 0.5), (L1 + L2 + 0.5))
ax.set_ylim(-(L1 + L2 + 0.5), (L1 + L2 + 0.5))
ax.set_aspect('equal')
ax.grid(True)
ax.set_title('Simulação de um Pêndulo Duplo')
ax.set_xlabel('Posição X (m)')
ax.set_ylabel('Posição Y (m)')

# Elementos da animação que serão atualizados
line, = ax.plot([], [], 'o-', lw=2, color='blue')
point1, = ax.plot([], [], 'o', markersize=10, color='red')
point2, = ax.plot([], [], 'o', markersize=10, color='green')
trace, = ax.plot([], [], '--', lw=1, color='gray', alpha=0.7)

history_x1, history_y1 = [], []
history_x2, history_y2 = [], []

def animate(i):
    current_x1 = [0, x1[i]]
    current_y1 = [0, y1[i]]
    current_x2 = [x1[i], x2[i]]
    current_y2 = [y1[i], y2[i]]

    line.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
    point1.set_data(x1[i], y1[i])
    point2.set_data(x2[i], y2[i])

    history_x1.append(x1[i])
    history_y1.append(y1[i])
    history_x2.append(x2[i])
    history_y2.append(y2[i])

    trace.set_data(history_x2, history_y2)  # Traço apenas do segundo pêndulo

    return line, point1, point2, trace

ani = FuncAnimation(fig, animate, frames=len(t_eval), interval=20, blit=True)

plt.show()