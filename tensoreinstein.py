import numpy as np
import sympy
import matplotlib.pyplot as plt
from einsteinpy.symbolic import SchwarzschildMetric

# Define as coordenadas
syms = sympy.symbols("t r theta phi")
t, r, theta, phi = syms

# Define a métrica de Schwarzschild
metric = SchwarzschildMetric(symbols=syms)

# O coeficiente g_rr da métrica de Schwarzschild
# Na notação padrão (t, r, theta, phi)
# g_rr é o elemento (1,1) da matriz da métrica (índices 0-based)
g_rr_expr = metric.tensor()[1, 1]

print(f"Expressão para g_rr: {g_rr_expr}")

# Substitua as constantes para valores numéricos para plotagem
# G = constante gravitacional, M = massa, c = velocidade da luz
G_val = 6.674e-11  # m^3 kg^-1 s^-2
M_val = 1.989e30   # Massa do Sol em kg
c_val = 2.998e8    # Velocidade da luz em m/s

# Calcule o raio de Schwarzschild (Rs)
Rs = (2 * G_val * M_val) / (c_val**2)
print(f"Raio de Schwarzschild (Rs) para a massa do Sol: {Rs:.2f} metros")

# Crie uma função numérica para g_rr
# Substitua G, M, c pelos valores e r pela variável numérica
g_rr_numeric_func = sympy.lambdify(r, g_rr_expr.subs({sympy.Symbol('G'): G_val, sympy.Symbol('M'): M_val, sympy.Symbol('c'): c_val}), 'numpy')

# Crie um array de valores para r (distância radial)
# Escolha um intervalo que inclua o raio de Schwarzschild, mas evite r=Rs para g_rr
# Vamos plotar de Rs * 1.001 (pouco depois do horizonte de eventos) até 10 * Rs
r_values = np.linspace(Rs * 1.001, 10 * Rs, 500) # Evita a singularidade em r=Rs

# Calcule os valores de g_rr para cada r
g_rr_values = g_rr_numeric_func(r_values)

# Crie o gráfico
plt.figure(figsize=(10, 6))
plt.plot(r_values, g_rr_values, label=r'$g_{rr} = (1 - \frac{2GM}{rc^2})^{-1}$')
plt.axvline(Rs, color='r', linestyle='--', label=f'Raio de Schwarzschild (Rs = {Rs:.2f} m)')
plt.title(r'Componente $g_{rr}$ da Métrica de Schwarzschild vs. Distância Radial')
plt.xlabel('Distância Radial $r$ (metros)')
plt.ylabel(r'Valor de $g_{rr}$')
plt.grid(True)
plt.ylim(0, 5) # Limita o eixo Y para melhor visualização, pois g_rr explode em Rs
plt.legend()
plt.show()

# --- Demonstração do Tensor de Einstein sendo zero no vácuo (para a métrica de Schwarzschild) ---
from einsteinpy.symbolic import EinsteinTensor
einstein_tensor = EinsteinTensor.from_metric(metric)

print("\nTensor de Einstein para a Métrica de Schwarzschild (no vácuo):")
# Vamos avaliar um componente, por exemplo G_00
G_00_expr = einstein_tensor.tensor()[0,0]
print(f"Componente G_00 (simbólico): {G_00_expr}")

# Se você tentar plotar G_00, verá que é sempre zero, ou seja, uma linha horizontal em 0.
# Isso confirma que a solução de Schwarzschild é uma solução de vácuo para as equações de campo de Einstein.