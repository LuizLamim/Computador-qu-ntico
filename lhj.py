def eh_primo(numero):
    """Verifica se um número é primo."""
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def encontrar_e_imprimir_primos(quantidade):
    """Encontra e imprime os primeiros 'quantidade' números primos."""
    primos_encontrados = 0
    numero_atual = 2  # O primeiro número primo é 2
    lista_primos = []

    while primos_encontrados < quantidade:
        if eh_primo(numero_atual):
            lista_primos.append(numero_atual)
            primos_encontrados += 1
        numero_atual += 1

    print(f"Os primeiros {quantidade} números primos são:")
    print(lista_primos)
    # Você também pode imprimi-los separados por vírgula se preferir
    # print(", ".join(map(str, lista_primos)))

# Chamada da função para obter os 11 primeiros números primos
quantidade_desejada = 11
encontrar_e_imprimir_primos(quantidade_desejada)