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