from decimal import Decimal, getcontext

def calcular_pi_precisao(casas_decimais):
    """Calcula o valor de π com a precisão especificada."""
    getcontext().prec = casas_decimais + 1  # +1 para o dígito antes da vírgula
    pi = Decimal(0)
    k = 0
    while True:
        termo = (Decimal(-1)**k) * (Decimal(1)/(2*k + 1))
        pi += termo
        if abs(termo) < Decimal(10)**(-casas_decimais - 2):  # Critério de parada
            break
        k += 1
    return 4 * pi

if __name__ == "__main__":
    precisao = 100
    valor_pi = calcular_pi_precisao(precisao)
    print(f"O valor de π com {precisao} casas decimais é:\n{valor_pi}")