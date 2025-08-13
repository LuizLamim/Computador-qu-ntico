# Importa a biblioteca matplotlib para plotar gráficos
import matplotlib.pyplot as plt

# Cria uma lista com os números de 1 a 10
x = list(range(1, 11))

# Calcula a tabuada do 5, multiplicando cada número da lista 'x' por 5
y = [i * 5 for i in x]

# Cria o gráfico
plt.plot(x, y, marker='o', linestyle='-', color='b')

# Adiciona o título ao gráfico
plt.title("Tabuada de Multiplicação do 5")

# Adiciona um rótulo ao eixo X
plt.xlabel("Multiplicador")

# Adiciona um rótulo ao eixo Y
plt.ylabel("Resultado")

# Adiciona uma grade para facilitar a leitura
plt.grid(True)

# Exibe o gráfico na tela
plt.show()

# Imprime a tabuada no console
print("Tabuada de Multiplicação do 5:")
for i in range(1, 11):
    resultado = 5 * i
    print(f"5 x {i} = {resultado}")