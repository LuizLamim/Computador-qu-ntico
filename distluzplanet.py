# Definindo a velocidade da luz em km/s
VELOCIDADE_LUZ_KM_POR_SEGUNDO = 299792.458

def calcular_tempo_viagem_luz():
    """
    Calcula o tempo que a luz leva para viajar da Terra a um planeta,
    dada a distância em quilômetros.
    """
    print("--- Calculadora de Tempo de Viagem da Luz ---")

    while True:
        try:
            distancia_km_str = input("Digite a distância entre a Terra e o planeta em quilômetros (ex: 150.000.000 para Marte): ")
            # Remover pontos e substituir vírgulas por pontos para garantir a conversão correta
            distancia_km_str = distancia_km_str.replace('.', '').replace(',', '.')
            distancia_km = float(distancia_km_str)

            if distancia_km < 0:
                print("A distância não pode ser negativa. Por favor, digite um valor válido.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a distância.")

    # Calcular o tempo em segundos
    tempo_segundos = distancia_km / VELOCIDADE_LUZ_KM_POR_SEGUNDO

    # Converter para outras unidades de tempo
    tempo_minutos = tempo_segundos / 60
    tempo_horas = tempo_minutos / 60
    tempo_dias = tempo_horas / 24

    print(f"\nDistância informada: {distancia_km:,.2f} km")
    print(f"Velocidade da luz: {VELOCIDADE_LUZ_KM_POR_SEGUNDO} km/s")
    print("\n--- Tempo de Viagem da Luz ---")
    print(f"Em segundos: {tempo_segundos:,.2f} s")
    print(f"Em minutos: {tempo_minutos:,.2f} min")
    print(f"Em horas: {tempo_horas:,.2f} h")
    print(f"Em dias: {tempo_dias:,.2f} dias")

if __name__ == "__main__":
    calcular_tempo_viagem_luz()