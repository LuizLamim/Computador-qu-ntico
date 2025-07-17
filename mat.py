import matplotlib.pyplot as plt
import numpy as np

# --- 1. Gráfico de Linha Simples ---
print("Gerando Gráfico de Linha Simples...")
plt.figure(figsize=(8, 6)) # Define o tamanho da figura (largura, altura em polegadas)
x = np.linspace(0, 10, 100) # Gera 100 pontos entre 0 e 10
y = np.sin(x) # Calcula o seno de x
plt.plot(x, y) # Cria o gráfico de linha
plt.title('Gráfico de Linha Simples (Seno)') # Título do gráfico
plt.xlabel('Eixo X') # Rótulo do eixo X
plt.ylabel('Eixo Y') # Rótulo do eixo Y
plt.grid(True) # Adiciona uma grade ao gráfico
plt.show() # Mostra o gráfico

# --- 2. Gráfico de Dispersão (Scatter Plot) ---
print("\nGerando Gráfico de Dispersão...")
plt.figure(figsize=(8, 6))
np.random.seed(42) # Para reprodutibilidade
x_scatter = np.random.rand(50) * 10
y_scatter = np.random.rand(50) * 10
sizes = np.random.rand(50) * 500 # Tamanho dos pontos
colors = np.random.rand(50) # Cores dos pontos
plt.scatter(x_scatter, y_scatter, s=sizes, c=colors, alpha=0.7, cmap='viridis') # Cria o gráfico de dispersão
plt.title('Gráfico de Dispersão')
plt.xlabel('Dados X')
plt.ylabel('Dados Y')
plt.colorbar(label='Intensidade de Cor') # Adiciona uma barra de cores
plt.show()

# --- 3. Gráfico de Barras ---
print("\nGerando Gráfico de Barras...")
plt.figure(figsize=(8, 6))
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [20, 35, 30, 45, 25]
plt.bar(categorias, valores, color='skyblue') # Cria o gráfico de barras
plt.title('Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.show()

# --- 4. Histograma ---
print("\nGerando Histograma...")
plt.figure(figsize=(8, 6))
dados_histograma = np.random.randn(1000) # Gera 1000 pontos de dados aleatórios (distribuição normal)
plt.hist(dados_histograma, bins=30, color='lightcoral', edgecolor='black') # Cria o histograma
plt.title('Histograma de Dados Aleatórios')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.show()

# --- 5. Múltiplos Gráficos em Uma Figura (Subplots) ---
print("\nGerando Múltiplos Gráficos (Subplots)...")
plt.figure(figsize=(12, 5))

# Primeiro subplot
plt.subplot(1, 2, 1) # 1 linha, 2 colunas, primeiro gráfico
plt.plot(x, y, color='purple')
plt.title('Seno')
plt.xlabel('X')
plt.ylabel('Y')

# Segundo subplot
plt.subplot(1, 2, 2) # 1 linha, 2 colunas, segundo gráfico
plt.plot(x, np.cos(x), color='green')
plt.title('Cosseno')
plt.xlabel('X')
plt.ylabel('Y')

plt.tight_layout() # Ajusta automaticamente os parâmetros do subplot para que caibam na área da figura
plt.show()

# --- 6. Personalização Avançada (Exemplo com Gráfico de Linha) ---
print("\nGerando Gráfico com Personalização Avançada...")
plt.figure(figsize=(10, 7))
y_line1 = np.exp(x / 2) # Função exponencial
y_line2 = x**2 # Função quadrática

plt.plot(x, y_line1, label='Exponencial ($e^{x/2}$)', color='blue', linestyle='--', linewidth=2, marker='o', markersize=4)
plt.plot(x, y_line2, label='Quadrática ($x^2$)', color='red', linestyle='-', linewidth=2, marker='x', markersize=4)

plt.title('Gráfico com Personalização Avançada', fontsize=16, fontweight='bold')
plt.xlabel('Eixo X', fontsize=12)
plt.ylabel('Eixo Y', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6) # Grid com estilo e transparência
plt.legend(fontsize=10) # Mostra a legenda
plt.text(2, 60, 'Ponto de Interesse', fontsize=10, color='darkgreen') # Adiciona texto ao gráfico
plt.annotate('Pico da exponencial', xy=(x[np.argmax(y_line1)], np.max(y_line1)),
             xytext=(5, 100), arrowprops=dict(facecolor='black', shrink=0.05)) # Adiciona uma anotação com seta

plt.yscale('log') # Escala logarítmica no eixo Y
plt.ylim(0.1, 1000) # Define limites para o eixo Y
plt.xlim(0, 8) # Define limites para o eixo X

plt.show()

print("\nDemonstração das funções básicas do Matplotlib concluída.")