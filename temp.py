def calcular_media_temperaturas():
  """
  Calcula a soma e a média de uma série de temperaturas fornecidas pelo usuário.
  O usuário decide quantas temperaturas serão inseridas.
  """
  temperaturas = []
  
  while True:
    try:
      quantidade = int(input("Quantas temperaturas você quer inserir para calcular a média? "))
      if quantidade > 0:
        break
      else:
        print("Por favor, digite um número maior que zero.")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número inteiro.")

  for i in range(quantidade):
    while True:
      try:
        temp = float(input(f"Digite a temperatura {i + 1}: "))
        temperaturas.append(temp)
        break
      except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

  if temperaturas:
    soma_temperaturas = sum(temperaturas)
    media_temperaturas = soma_temperaturas / len(temperaturas)

    print(f"\nA soma total das temperaturas é: {soma_temperaturas:.2f}°C")
    print(f"A média das temperaturas é: {media_temperaturas:.2f}°C")
  else:
    print("Nenhuma temperatura foi inserida para o cálculo.")

# Executar o programa
if __name__ == "__main__":
  calcular_media_temperaturas()