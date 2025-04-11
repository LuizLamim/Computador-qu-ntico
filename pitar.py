import math

def calcular_lado_triangulo_retangulo():
    """
    Recebe dois lados de um triângulo retângulo e calcula o lado faltante
    usando o teorema de Pitágoras.
    """
    lados = []
    print("Por favor, insira o valor de dois lados do triângulo retângulo.")
    print("Deixe o lado desconhecido com valor 0.")

    for i in range(3):
        while True:
            try:
                lado = float(input(f"Digite o valor do lado {i+1}: "))
                lados.append(lado)
                break
            except ValueError:
                print("Por favor, digite um valor numérico válido.")

    a, b, c = sorted(lados)  # Ordena para facilitar a identificação da hipotenusa

    if c == 0:  # Hipotenusa desconhecida
        if a == 0 or b == 0:
            print("Você precisa fornecer o valor de dois lados para calcular o terceiro.")
        else:
            c_quadrado = a**2 + b**2
            c = math.sqrt(c_quadrado)
            print(f"A hipotenusa (o lado faltante) é: {c:.2f}")
    elif a == 0:  # Um dos catetos desconhecido
        if c == 0 or b == 0:
            print("Você precisa fornecer o valor de dois lados para calcular o terceiro.")
        elif c <= b:
            print("A hipotenusa deve ser maior que o cateto conhecido.")
        else:
            a_quadrado = c**2 - b**2
            a = math.sqrt(a_quadrado)
            print(f"Um dos catetos (o lado faltante) é: {a:.2f}")
    elif b == 0:  # O outro cateto desconhecido
        if c == 0 or a == 0:
            print("Você precisa fornecer o valor de dois lados para calcular o terceiro.")
        elif c <= a:
            print("A hipotenusa deve ser maior que o cateto conhecido.")
        else:
            b_quadrado = c**2 - a**2
            b = math.sqrt(b_quadrado)
            print(f"Um dos catetos (o lado faltante) é: {b:.2f}")
    else:
        print("Você já forneceu os três lados do triângulo.")

if __name__ == "__main__":
    calcular_lado_triangulo_retangulo()