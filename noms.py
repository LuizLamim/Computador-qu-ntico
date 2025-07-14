def coletar_nomes():
    """
    Coleta 5 nomes de pessoas do usuário e os armazena em uma lista.

    Retorna:
        list: Uma lista contendo os 5 nomes inseridos.
    """
    nomes = []
    print("Por favor, digite 5 nomes de pessoas:")
    for i in range(5):
        while True:
            nome = input(f"Nome {i+1}: ").strip()
            if nome:  # Verifica se o nome não está vazio
                nomes.append(nome)
                break
            else:
                print("O nome não pode estar vazio. Por favor, digite um nome válido.")
    return nomes

# Chama a função para coletar os nomes
lista_de_nomes = coletar_nomes()

# Exibe os nomes coletados
print("\nOs nomes que você digitou são:")
for nome in lista_de_nomes:
    print(nome)