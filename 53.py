import matplotlib.pyplot as plt
import numpy as np

# 1. Definir quantos números você quer (neste caso, 53)
NUM_ELEMENTOS = 53

# 2. Gerar os 53 primeiros números inteiros (de 1 a 53)
# O np.arange(1, NUM_ELEMENTOS + 1) cria um array [1, 2, ..., 53]
numeros = np.arange(1, NUM_ELEMENTOS + 1)

# 3. Preparar o gráfico

# Cria a figura (janela) e os eixos do gráfico
fig, ax = plt.subplots()

# Plota os números. 
# Usamos 'numeros' tanto para o eixo X quanto para o eixo Y
# para que o gráfico plote os pontos (1,1), (2,2), ..., (53,53).
# 'b-' é para uma linha azul contínua (Blue line)
# 'o' é para adicionar um círculo em cada ponto (Optional marker)
ax.plot(numeros, numeros, 'bo-', label='Números de 1 a 53')