def is_prime(num):
    """Verifica se um número é primo."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_first_n_primes(n):
    """Calcula a soma dos primeiros n números primos."""
    prime_count = 0
    num = 2
    total_sum = 0
    primes = [] # Opcional: para armazenar e exibir os primos encontrados

    while prime_count < n:
        if is_prime(num):
            total_sum += num
            primes.append(num) # Adiciona o primo à lista (opcional)
            prime_count += 1
        num += 1
    return total_sum, primes # Retorna a soma e a lista de primos (opcional)

# Definimos quantos números primos queremos somar
quantidade_primos = 25

# Chamamos a função para calcular a soma
soma_total, lista_primos = sum_first_n_primes(quantidade_primos)

# Exibimos o resultado
print(f"Os primeiros {quantidade_primos} números primos são: {lista_primos}")
print(f"A soma dos primeiros {quantidade_primos} números primos é: {soma_total}")