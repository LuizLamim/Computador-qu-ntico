def calcular_media_pesos():
  """
  Calcula a soma e a média de uma lista de 10 pesos fornecidos pelo usuário.
  """
  pesos = []
  for i in range(10):
    while True:
      try:
        peso = float(input(f"Digite o peso da pessoa {i + 1} (em kg): "))
        if peso > 0:
          pesos.append(peso)
          break
        else:
          print("Por favor, digite um peso válido (maior que zero).")
      except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

  soma_pesos = sum(pesos)
  media_pesos = soma_pesos / len(pesos)

  print(f"\nA soma total dos pesos é: {soma_pesos:.2f} kg")
  print(f"A média dos pesos é: {media_pesos:.2f} kg")

# Executar o programa
if __name__ == "__main__":
  calcular_media_pesos()