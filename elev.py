def calcular_potencia():
    print("--- Calculadora de Potência ---")
    
    try:
        base = float(input("Digite o número base: "))
        expoente = float(input("Digite o expoente (para elevar): "))

        resultado = base ** expoente

        print(f"\nResultado: {base} elevado a {expoente} é igual a {resultado}")
        
    