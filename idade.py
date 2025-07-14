def coletar_idades():
    """
    Coleta 5 idades de pessoas do usuário e as armazena em uma lista.

    Retorna:
        list: Uma lista contendo as 5 idades inseridas.
    """
    idades = []
    print("Por favor, digite 5 idades:")
    for i in range(5):
        while True:
            try:
                idade = int(input(f"Idade {i+1}: ").strip())
                if idade > 0:  # Verifica se a idade é um número positivo
                    idades.append(idade)
                    break
                else:
                    print("A idade deve ser um número positivo. Por favor, digite novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para a idade.")
    return idades

# Chama a função para coletar as idades
lista_de_idades = coletar_idades()

# Exibe as idades coletadas
print("\nAs idades que você digitou são:")
for idade in lista_de_idades:
    print(idade)