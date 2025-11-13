def somar_numeros():
    try:
        numero1 = float(input("Digite o primeiro número: "))

        numero2 = float(input("Digite o segundo número: "))

        soma = numero1 + numero2

        print(f"\nA soma de {numero1} e {numero2} é: {soma}")

    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos.")

