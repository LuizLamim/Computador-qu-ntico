# Importa a biblioteca matplotlib para a criação de gráficos
import matplotlib.pyplot as plt

# Cria uma lista com os números de 1 a 10 (os multiplicadores)
multiplicadores = list(range(1, 11))

# Calcula a tabuada do 7, gerando uma lista com os resultados
resultados = [7 * i for i in multiplicadores]

# Cria o gráfico de linha
plt.plot(multiplicadores, resultados, marker='o', linestyle='-', color='purple')

# Adiciona título e rótulos aos eixos do gráfico
plt.title("Tabuada de Multiplicação do 7")
plt.xlabel("Multiplicador")
plt.ylabel("Resultado")

# Adiciona uma grade para facilitar a leitura dos valores
plt.grid(True)

# Exibe o gráfico em uma janela
plt.show()

# Imprime a tabuada no console para referência
print("Tabuada de Multiplicação do 7:")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")