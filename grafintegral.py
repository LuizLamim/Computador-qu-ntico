import numpy as np
import matplotlib.pyplot as plt

# 1. Definir a função matemática
def f(x):
    return x**2 + np.cos(x)

# 2. Configurar o intervalo do eixo X (Domínio total do gráfico)
# np.linspace cria 1000 pontos igualmente espaçados entre -2 e 6
x = np.linspace(-2, 6, 1000)
y = f(x)

# 3. Configurar o intervalo da INTEGRAL (Onde vamos pintar)
# Vamos integrar de 0 a 5, como no exemplo anterior
x_area = np.linspace(0, 5, 1000)
y_area = f(x_area)

# 4. Criar o gráfico
plt.figure(figsize=(10, 6))

# Desenhar a linha principal da função
plt.plot(x, y, color='blue', linewidth=2, label=r'$f(x) = x^2 + \cos(x)$')

# A MÁGICA: Preencher a área sob a curva
plt.fill_between(x_area, y_area, color='skyblue', alpha=0.4, label='Área Integrada (0 a 5)')

# 5. Estética (Eixos, Título, Grade)
plt.title("Visualização Geométrica da Integral Definida", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)

# Adicionar linhas dos eixos X e Y (para ficar parecendo caderno de cálculo)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.grid(True, linestyle='--', alpha=0.6) # Grade pontilhada
plt.legend() # Mostrar a legenda

# Mostrar o gráfico
plt.show()