def eh_primo(numero):
    """Verifica se um número é primo."""

    if numero <= 1:
        return False  # Números menores ou iguais a 1 não são primos

    # Verifica divisibilidade de 2 até a raiz quadrada do número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # Se for divisível, não é primo

    return True  # Se não for divisível por nenhum número, é primo

# Exemplo de uso
numero = int(input("Digite um número: "))

if eh_primo(numero):
    print(numero, "é um número primo")
else:
    print(numero, "não é um número primo")