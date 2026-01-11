import numpy as np
import matplotlib.pyplot as plt

m = 70000.0        # Massa (kg)
thrust = 240000.0  # Empuxo total dos motores (N)
rho = 1.225        # Densidade do ar (kg/m^3)
S = 125.0          # Área das asas (m^2)
Cd = 0.03          # Coeficiente de arrasto
Cl = 0.5           # Coeficiente de sustentação (durante a corrida)
mu = 0.02          # Coeficiente de atrito de rolamento
g = 9.81           # Gravidade (m/s^2)

dt = 0.1           # Intervalo de tempo (segundos)
v = 0.0            # Velocidade inicial
x = 0.0            # Posição inicial
v_decolagem = 80   # Velocidade de rotação (m/s) (~290 km/h)

tempos = []
aceleracoes = []
velocidades = []

t = 0
while v < v_decolagem:
    # 1. Cálculo das forças aerodinâmicas
    sustentacao = 0.5 * rho * v**2 * S * Cl
    arrasto = 0.5 * rho * v**2 * S * Cd
    
    # 2. Atrito de rolamento (P = m*g. Força Normal = Peso - Sustentação)
    forca_normal = max(0, (m * g) - sustentacao)
    atrito = mu * forca_normal
    
    # 3. Segunda Lei de Newton (F_resultante = m * a)
    # F_res = Empuxo - Arrasto - Atrito
    forca_resultante = thrust - arrasto - atrito
    a = forca_resultante / m
    
    # Armazenar dados
    tempos.append(t)
    aceleracoes.append(a)
    velocidades.append(v)
    
    # Atualizar velocidade e tempo
    v += a * dt
    t += dt

# Criação dos Gráficos
plt.figure(figsize=(10, 8))

# Gráfico de Aceleração
plt.subplot(2, 1, 1)
plt.plot(tempos, aceleracoes, 'r-', linewidth=2, label='Aceleração (m/s²)')
plt.title('Dinâmica de Decolagem do Avião')
plt.ylabel('Aceleração (m/s²)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Gráfico de Velocidade
plt.subplot(2, 1, 2)
plt.plot(tempos, velocidades, 'b-', linewidth=2, label='Velocidade (m/s)')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.tight_layout()
plt.show()