import matplotlib.pyplot as plt

def plotar_quadrado():
  """
  Plota um gráfico de um quadrado com lado 1.
  """
  # Coordenadas dos vértices do quadrado
  # [x1, x2, x3, x4, x1] para fechar a forma
  x_coords = [0, 1, 1, 0, 0]
  y_coords = [0, 0, 1, 1, 0]

  # Criar o gráfico
  plt.figure()


  plt.plot(x_coords, y_coords, marker='o')

  # Configurar o título e os rótulos dos eixos
  plt.title("Gráfico de um Quadrado (Lado 1)")
  plt.xlabel("Eixo X")
  plt.ylabel("Eixo Y")

  # Garantir que os eixos tenham a mesma escala para que o quadrado não pareça distorcido
  plt.axis('equal')

  # Adicionar uma grade para facilitar a visualização
  plt.grid(True)

  # Exibir o gráfico
  plt.show()
plotar_quadrado()