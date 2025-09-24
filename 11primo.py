import matplotlib.pyplot as plt

def gerar_primos(n):
    """
    Gera uma lista com os primeiros 'n' números primos.
    """
    # Inicializa a lista de primos
    primos = []
    # Começa a busca a partir do número 2 (o primeiro primo)
    numero_candidato = 2

    while len(primos) < n:
        
        eh_primo = True

        for divisor in range(2, int(numero_candidato**0.5) + 1):
            if numero_candidato % divisor == 0:
                # Se encontrar um divisor, não é primo
                eh_primo = False
                # Pula para o próximo número candidato
                break

        
        # Se o loop terminar e 'eh_primo' ainda for True, adiciona à lista
        if eh_primo:
            primos.append(numero_candidato)

        # Passa para o próximo número
        numero_candidato += 1

    return primos

# --- PARTE PRINCIPAL DO PROGRAMA ---

# 1. Geração dos 11 primeiros primos
quantidade_desejada = 11
primos = gerar_primos(quantidade_desejada)

# Os números que representam a ordem (1º, 2º, 3º, ...)
ordem = list(range(1, quantidade_desejada + 1))

# 2. Plotagem dos resultados
print(f"Os {quantidade_desejada} primeiros números primos são: {primos}")

# Cria a figura e os eixos
plt.figure(figsize=(10, 6))

# Plota os pontos
# 'o-' cria uma linha que conecta os pontos (marcados com 'o')
plt.plot(ordem, primos, marker='o', linestyle='-', color='blue', label='Números Primos')

# Adiciona os valores dos primos acima dos pontos
for i in range(quantidade_desejada):
    plt.text(ordem[i], primos[i] + 0.5, str(primos[i]), ha='center', fontsize=9)

# Configurações do gráfico
plt.title(f'Os Primeiros {quantidade_desejada} Números Primos', fontsize=14)
plt.xlabel('Ordem do Primo (n)', fontsize=12)
plt.ylabel('Valor do Primo', fontsize=12)
plt.xticks(ordem) # Define os rótulos do eixo X para as ordens
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Exibe o gráfico
plt.show()