def calcular_media(num1, num2):

    media = (num1 + num2) / 2
    return media

def main():
    # Bloco principal para interação com o usuário

    print("--- Calculadora de Média entre Dois Números ---")

    try:
        # 1. Solicita o primeiro número
        entrada_numero_1 = input("Digite o primeiro número: ")
        numero1 = float(entrada_numero_1)

        # 2. Solicita o segundo número
        entrada_numero_2 = input("Digite o segundo número: ")
        numero2 = float(entrada_numero_2)

        # 3. Chama a função para calcular a média
        resultado_media = calcular_media(numero1, numero2)

        # 4. Exibe o resultado formatado
        print("-" * 40)
        print(f"Os números digitados foram: {numero1} e {numero2}")
        print(f"A média aritmética entre {numero1} e {numero2} é: {resultado_media:.2f}")
        print("-" * 40)

    except ValueError:
        # Trata o erro caso o usuário digite algo que não seja um número
        print("\nErro: Por favor, digite apenas valores numéricos válidos.")
    except Exception as e:
        # Trata outros erros inesperados
        print(f"\nOcorreu um erro inesperado: {e}")
