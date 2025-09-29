def somar_equacoes_primeiro_grau():
    """
    Calcula a soma de duas equações de primeiro grau (y = ax + b).
    A função solicita os coeficientes (a e b) de cada equação.
    """
    print("--- Soma de Duas Equações de Primeiro Grau (y = ax + b) ---")

    # Coeficientes da Primeira Equação (y1 = a1*x + b1)
    print("\n--- Primeira Equação (y1 = a1*x + b1) ---")
    try:
        a1 = float(input("Digite o coeficiente 'a' (inclinacao) da primeira equação: "))
        b1 = float(input("Digite o coeficiente 'b' (intercepto y) da primeira equação: "))
    except ValueError:
        print("\nERRO: Por favor, insira apenas números.")
        return