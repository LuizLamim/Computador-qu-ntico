def calcular_queda_livre():
    print("--- Calculadora de Queda Livre ---")
    print("Este programa calcula a distância percorrida e a velocidade final")
    print("de um objeto caindo no vácuo (ignorando a resistência do ar).\n")

    try:
        # 1. Definindo a constante da gravidade (Terra)
        g = 9.81  # m/s^2

        # 2. Recebendo o tempo de queda do usuário
        tempo = float(input("Digite o tempo de queda (em segundos): "))

        if tempo < 0:
            print("O tempo não pode ser negativo!")
            return

        # 3. Realizando os cálculos
        # Fórmula da distância: d = (1/2) * g * t^2
        distancia = 0.5 * g * (tempo ** 2)

        # Fórmula da velocidade: v = g * t
        velocidade = g * tempo

        # Convertendo velocidade para km/h (opcional, mas útil)
        velocidade_kmh = velocidade * 3.6

        # 4. Exibindo os resultados
        print("\n--- Resultados ---")
        print(f"Tempo de queda: {tempo} segundos")
        print(f"Distância percorrida (Altura): {distancia:.2f} metros")
        print(f"Velocidade final: {velocidade:.2f} m/s")
        print(f"Velocidade final: {velocidade_kmh:.2f} km/h")

    except ValueError:
        print("Erro: Por favor, digite apenas números válidos (use ponto para decimais).")

# Executa o programa
if __name__ == "__main__":
    calcular_queda_livre()