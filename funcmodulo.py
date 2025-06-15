import numpy as np
import matplotlib.pyplot as plt

# 1. Definir o intervalo para x
# Gerar 1000 pontos igualmente espaçados entre -2*pi e 2*pi
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 2. Calcular os valores de y usando a função seno e depois aplicar o valor absoluto
y_sen = np.sin(x)
y_mod_sen = np.abs(y_sen) # Aplica o valor absoluto

# 3. Criar o gráfico
plt.figure(figsize=(10, 6)) # Define o tamanho da figura

# Plota a função seno original (opcional, para comparação)
# plt.plot(x, y_sen, label='sen(x)', color='gray', linestyle='--', alpha=0.6)

# Plota a função modular de seno
plt.plot(x, y_mod_sen, label='|sen(x)|', color='red')

# 4. Adicionar rótulos e título
plt.title('Gráfico da Função Modular de Seno (|sen(x)|)')
plt.xlabel('x (radianos)')
plt.ylabel('|sen(x)|')

# 5. Adicionar a grade para melhor visualização
plt.grid(True)

# 6. Adicionar a linha do eixo x em y=0 e a linha do eixo y em x=0
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# 7. Adicionar a legenda
plt.legend()

# 8. Definir limites do eixo Y para melhor visualização (opcional)
plt.ylim(-0.1, 1.1)

# 9. Mostrar o gráfico
plt.show()