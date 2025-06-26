def eh_primo(num):
    """
    Verifica se um número é primo.
    Um número é primo se for maior que 1 e não tiver divisores,
    exceto 1 e ele mesmo.
    """
    if num <= 1:
        return False
    # Itera de 2 até a raiz quadrada do número.
    # Se encontrar um divisor nesse intervalo, não é primo.
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def encontrar_primeiros_primos(quantidade):
    """
    Encontra uma determinada quantidade de números primos.
    """
    primos = []
    numero_atual = 2
    while len(primos) < quantidade:
        if eh_primo(numero_atual):
            primos.append(numero_atual)
        numero_atual += 1
    return primos

# Encontrar os primeiros 10 números primos
primeiros_10_primos = encontrar_primeiros_primos(10)
print(f"Os primeiros 10 números primos são: {primeiros_10_primos}")