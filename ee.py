import math

def calcular_excentricidade_elipse():
    """
    Calcula a excentricidade de uma elipse.
    Permite escolher entre inserir semieixo maior/menor ou semieixo maior/distância focal.
    """
    print("--- Calculadora de Excentricidade de Elipse ---")
    print("Selecione a opção de entrada de dados:")
    print("1. Semieixo maior (a) e Semieixo menor (b)")
    print("2. Semieixo maior (a) e Distância focal (c)")

    while True:
        opcao = input("Digite 1 ou 2: ")
        if opcao in ['1', '2']:
            break
        else:
            print("Opção inválida. Por favor, digite 1 ou 2.")

    try:
        if opcao == '1':
            a = float(input("Digite o valor do semieixo maior (a): "))
            b = float(input("Digite o valor do semieixo menor (b): "))

            if not (a > 0 and b > 0):
                raise ValueError("Os valores dos semieixos devem ser positivos.")
            if b >= a:
                raise ValueError("O semieixo menor (b) deve ser menor que o semieixo maior (a) para uma elipse.")

            c = math.sqrt(a**2 - b**2)
            excentricidade = c / a

        else: # opcao == '2'
            a = float(input("Digite o valor do semieixo maior (a): "))
            c = float(input("Digite o valor da distância focal (c): "))

            if not (a > 0 and c >= 0):
                raise ValueError("O semieixo maior deve ser positivo e a distância focal não negativa.")
            if c >= a:
                raise ValueError("A distância focal (c) deve ser menor que o semieixo maior (a) para uma elipse.")

            excentricidade = c / a

        print(f"\nO semieixo maior (a) é: {a:.4f}")
        if opcao == '1':
            print(f"O semieixo menor (b) é: {b:.4f}")
            print(f"A distância focal (c) calculada é: {c:.4f}")
        else:
            print(f"A distância focal (c) é: {c:.4f}")

        print(f"\nA excentricidade da elipse é: {excentricidade:.4f}")

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Chama a função para executar o programa
if __name__ == "__main__":
    calcular_excentricidade_elipse()