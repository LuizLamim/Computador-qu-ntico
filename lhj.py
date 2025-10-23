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