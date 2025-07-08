def imprimir_alfabeto():
    """Imprime o alfabeto em letras minúsculas e maiúsculas."""

    print("Alfabeto em letras minúsculas:")
    for i in range(ord('a'), ord('z') + 1):
        print(chr(i), end=" ")
    print("\n") # Nova linha para separar

    print("Alfabeto em letras maiúsculas:")
    for i in range(ord('A'), ord('Z') + 1):
        print(chr(i), end=" ")
    print("\n") # Nova linha para o final

# Chama a função para executar o programa
if __name__ == "__main__":
    imprimir_alfabeto()