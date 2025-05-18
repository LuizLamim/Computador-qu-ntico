def calcular_coeficiente_angular():
  """Calcula o coeficiente angular de uma reta dados dois pontos."""
  try:
    x1 = float(input("Digite a coordenada x do primeiro ponto: "))
    y1 = float(input("Digite a coordenada y do primeiro ponto: "))
    x2 = float(input("Digite a coordenada x do segundo ponto: "))
    y2 = float(input("Digite a coordenada y do segundo ponto: "))

    if x1 == x2:
      return "A reta é vertical e o coeficiente angular é indefinido."
    else:
      coeficiente_angular = (y2 - y1) / (x2 - x1)
      return f"O coeficiente angular da reta é: {coeficiente_angular}"

  except ValueError:
    return "Entrada inválida. Por favor, digite números para as coordenadas."

# Chama a função para executar o cálculo
resultado = calcular_coeficiente_angular()
print(resultado)