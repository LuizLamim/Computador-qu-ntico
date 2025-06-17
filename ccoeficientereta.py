def calcular_coeficiente_angular(x1, y1, x2, y2):
    """
    Calcula o coeficiente angular (inclinação) de uma reta dados dois pontos.

    Args:
        x1 (float): Coordenada x do primeiro ponto.
        y1 (float): Coordenada y do primeiro ponto.
        x2 (float): Coordenada x do segundo ponto.
        y2 (float): Coordenada y do segundo ponto.

    Returns:
        float or str: O coeficiente angular se a reta não for vertical,
                      ou uma mensagem de erro se for vertical.
    """
    if x2 - x1 == 0:
        return "A reta é vertical. O coeficiente angular é indefinido."
    else:
        coeficiente = (y2 - y1) / (x2 - x1)
        return coeficiente

# --- Parte principal do programa ---
if __name__ == "__main__":
    print("Vamos calcular o coeficiente angular de uma reta!")

    try:
        # Solicita as coordenadas do primeiro ponto
        x1 = float(input("Digite a coordenada x do primeiro ponto: "))
        y1 = float(input("Digite a coordenada y do primeiro ponto: "))

        # Solicita as coordenadas do segundo ponto
        x2 = float(input("Digite a coordenada x do segundo ponto: "))
        y2 = float(input("Digite a coordenada y do segundo ponto: "))

        # Chama a função para calcular o coeficiente angular
        resultado = calcular_coeficiente_angular(x1, y1, x2, y2)

        # Exibe o resultado
        if isinstance(resultado, str):
            print(f"Erro: {resultado}")
        else:
            print(f"O coeficiente angular da reta é: {resultado:.2f}")

    except ValueError:
        print("Entrada inválida. Por favor, digite números para as coordenadas.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")