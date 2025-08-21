import math

def calcular_curvatura(distancia_km):
    """
    Calcula a curvatura da Terra (queda vertical) para uma determinada distância.

    Args:
        distancia_km (float): A distância em quilômetros.

    Returns:
        float: A queda vertical em metros.
    """
    # Raio médio da Terra em quilômetros
    raio_terra_km = 6371.0

    # Calcula a queda vertical em quilômetros
    queda_vertical_km = (distancia_km**2) / (2 * raio_terra_km)

    # Converte a queda vertical para metros para uma leitura mais fácil
    queda_vertical_metros = queda_vertical_km * 1000

    return queda_vertical_metros

def main():
    """
    Função principal para executar o programa.
    """
    print("--- Calculadora de Curvatura da Terra ---")
    print("Este programa calcula a queda vertical (curvatura) da Terra ")
    print("para uma determinada distância.")
    print("------------------------------------------")

    try:
        distancia = float(input("Digite a distância em quilômetros: "))
        if distancia < 0:
            print("Por favor, digite um valor positivo.")
            return

        curvatura_em_metros = calcular_curvatura(distancia)

        print(f"\nPara uma distância de {distancia} km, a curvatura (queda vertical) é de:")
        print(f"{curvatura_em_metros:.2f} metros.")
        print("\n*Este cálculo é uma aproximação e desconsidera fatores como refração atmosférica.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    main()