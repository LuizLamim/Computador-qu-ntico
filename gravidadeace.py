import numpy as np
import matplotlib.pyplot as plt

# Definindo constantes
G = 6.67430e-11  # Constante gravitacional universal em m^3 kg^-1 s^-2
M = 5.972e24     # Massa da Terra em kg
R = 6.371e6      # Raio médio da Terra em m

# Criando um array de distâncias do centro da Terra (em metros)
# A faixa vai de 0 (centro) a 3 * R (três vezes o raio da Terra)
distancia = np.linspace(0, 3 * R, 1000)

# Criando um array para a aceleração da gravidade
aceleracao_gravidade = np.zeros_like(distancia)

# Loop para calcular a aceleração da gravidade
for i, r in enumerate(distancia):
    if r < R:
        # Aceleração da gravidade dentro da Terra
        # A gravidade aumenta linearmente com a distância do centro
        aceleracao_gravidade[i] = (G * M * r) / (R**3)
    else:
        # Aceleração da gravidade fora da Terra
        # A gravidade diminui com o inverso do quadrado da distância
        aceleracao_gravidade[i] = (G * M) / (r**2)

# Plotando o gráfico
plt.style.use('dark_background')  # Estilo de gráfico com fundo escuro
plt.figure(figsize=(10, 6))       # Tamanho da figura

plt.plot(distancia / 1000, aceleracao_gravidade, color='red', linewidth=2)
plt.title('Aceleração da Gravidade vs. Distância do Centro da Terra', fontsize=16)
plt.xlabel('Distância do Centro da Terra (km)', fontsize=12)
plt.ylabel('Aceleração da Gravidade ($m/s^2$)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Adicionando linhas e textos para pontos importantes
plt.axvline(x=R/1000, color='gray', linestyle='--', label='Superfície da Terra')
plt.text(R/1000 + 100, 10, 'Superfície da Terra', rotation=90, color='white')
plt.axhline(y=9.81, color='green', linestyle=':', label='Valor Padrão (9.81 $m/s^2$)')

# Criando anotações para o centro da Terra e o valor na superfície
plt.annotate('Centro da Terra', xy=(0, 0), xytext=(2000, 2),
             arrowprops=dict(facecolor='white', shrink=0.05),
             fontsize=10, color='white')

plt.annotate('Aceleração Máxima na Superfície', xy=(R/1000, 9.81), xytext=(8000, 12),
             arrowprops=dict(facecolor='white', shrink=0.05),
             fontsize=10, color='white')

plt.legend()
plt.tight_layout() # Ajusta o layout para evitar sobreposição de elementos
plt.show()