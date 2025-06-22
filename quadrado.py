def calcular_area_quadrado(lado):
  """
  Calcula a área de um quadrado dado o comprimento do seu lado.

  Args:
    lado: O comprimento do lado do quadrado (pode ser um número inteiro ou decimal).

  Returns:
    A área do quadrado.
  """
  if lado < 0:
    return "O comprimento do lado não pode ser negativo."
  else:
    area = lado * lado
    return area

# --- Exemplo de uso ---
if __name__ == "__main__":
  try:
    lado_do_quadrado = float(input("Digite o comprimento do lado do quadrado: "))
    
    area_calculada = calcular_area_quadrado(lado_do_quadrado)
    
    if isinstance(area_calculada, str): # Verifica se é a mensagem de erro
      print(area_calculada)
    else:
      print(f"A área do quadrado com lado {lado_do_quadrado} é: {area_calculada}")

  except ValueError:
    print("Entrada inválida. Por favor, digite um número.")