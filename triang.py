def calcular_area_triangulo_retangulo(cateto1, cateto2):
  """
  Calcula a área de um triângulo retângulo dados os comprimentos dos dois catetos.

  Args:
    cateto1: O comprimento do primeiro cateto.
    cateto2: O comprimento do segundo cateto.

  Returns:
    A área do triângulo retângulo ou uma mensagem de erro se os catetos forem inválidos.
  """
  if cateto1 < 0 or cateto2 < 0:
    return "Os comprimentos dos catetos não podem ser negativos."
  elif cateto1 == 0 or cateto2 == 0:
    return "Para formar um triângulo, ambos os catetos devem ser maiores que zero."
  else:
    area = (cateto1 * cateto2) / 2
    return area

# --- Exemplo de uso ---
if __name__ == "__main__":
  try:
    cateto_a = float(input("Digite o comprimento do primeiro cateto: "))
    cateto_b = float(input("Digite o comprimento do segundo cateto: "))
    
    area_calculada = calcular_area_triangulo_retangulo(cateto_a, cateto_b)
    
    if isinstance(area_calculada, str): # Verifica se é uma mensagem de erro
      print(area_calculada)
    else:
      print(f"A área do triângulo retângulo com catetos {cateto_a} e {cateto_b} é: {area_calculada}")

  except ValueError:
    print("Entrada inválida. Por favor, digite números para os catetos.")