# Criando uma matriz 3x3 com valores predefinidos
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz 1:")
for linha in matriz1:
    print(linha)

# ---

# Criando uma matriz 3x3 preenchida com zeros
matriz2 = [[0 for _ in range(3)] for _ in range(3)]

print("\nMatriz 2 (preenchida com zeros):")
for linha in matriz2:
    print(linha)

# ---

# Criando uma matriz 3x3 com entrada do usuário
matriz3 = []
print("\nDigite os elementos da matriz 3x3 (um por linha, separados por espaço):")
for i in range(3):
    linha = []
    while True:
        entrada = input(f"Linha {i+1}: ").strip().split()
        if len(entrada) == 3 and all(item.isdigit() or (item[0] == '-' and item[1:].isdigit()) for item in entrada):
            linha = [int(item) for item in entrada]
            break
        else:
            print("Entrada inválida. Por favor, digite 3 números inteiros separados por espaço.")
    matriz3.append(linha)

print("\nMatriz 3 (criada pelo usuário):")
for linha in matriz3:
    print(linha)