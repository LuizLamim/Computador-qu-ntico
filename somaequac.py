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
    
    # Coeficientes da Segunda Equação (y2 = a2*x + b2)
    print("\n--- Segunda Equação (y2 = a2*x + b2) ---")
    try:
        a2 = float(input("Digite o coeficiente 'a' (inclinacao) da segunda equação: "))
        b2 = float(input("Digite o coeficiente 'b' (intercepto y) da segunda equação: "))
    except ValueError:
        print("\nERRO: Por favor, insira apenas números.")
        return

    # Cálculo da Equação Soma (y_soma = a_soma*x + b_soma)
    # Soma dos coeficientes 'a'
    a_soma = a1 + a2
    # Soma dos coeficientes 'b'
    b_soma = b1 + b2