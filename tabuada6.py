# Importa a biblioteca matplotlib para criar o gráfico
import matplotlib.pyplot as plt

# Define os valores para o eixo X (os multiplicadores de 1 a 10)
multiplicadores = list(range(1, 11))

# Calcula a tabuada do 6 para cada multiplicador
resultados = [6 * i for i in multiplicadores]

# Cria o gráfico de linha
plt.plot(multiplicadores, resultados, marker='o', linestyle='-', color='g')

# Adiciona título e rótulos aos eixos
plt.title("Tabuada de Multiplicação do 6")
plt.xlabel("Multiplicador")
plt.ylabel("Resultado")

# Adiciona uma grade ao fundo do gráfico
plt.grid(True)

# Exibe a janela do gráfico
plt.show()

# Imprime a tabuada no console para referência
print("Tabuada de Multiplicação do 6:")
for i in range(1, 11):
    print(f"6 x {i} = {6 * i}")