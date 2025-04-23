import random

def gera_tabuleiro_vazio():
    """Gera um tabuleiro de Sudoku 9x9 vazio."""
    return [[0 for _ in range(9)] for _ in range(9)]

def eh_valido(tabuleiro, linha, coluna, numero):
    """Verifica se um número é válido em uma determinada posição."""
    # Verifica a linha
    for c in range(9):
        if tabuleiro[linha][c] == numero:
            return False

    # Verifica a coluna
    for l in range(9):
        if tabuleiro[l][coluna] == numero:
            return False

    # Verifica o bloco 3x3
    bloco_linha = linha // 3
    bloco_coluna = coluna // 3
    for l in range(bloco_linha * 3, bloco_linha * 3 + 3):
        for c in range(bloco_coluna * 3, bloco_coluna * 3 + 3):
            if tabuleiro[l][c] == numero:
                return False

    return True

def encontra_vazio(tabuleiro):
    """Encontra a primeira célula vazia (com valor 0) no tabuleiro."""
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                return linha, coluna
    return None

def resolve_sudoku(tabuleiro):
    """Resolve o tabuleiro de Sudoku usando backtracking."""
    encontrar = encontra_vazio(tabuleiro)
    if not encontrar:
        return True  # Tabuleiro está completo

    linha, coluna = encontrar

    for numero in range(1, 10):
        if eh_valido(tabuleiro, linha, coluna, numero):
            tabuleiro[linha][coluna] = numero

            if resolve_sudoku(tabuleiro):
                return True

            tabuleiro[linha][coluna] = 0  # Backtrack

    return False

def remove_celulas(tabuleiro, dificuldade):
    """Remove algumas células do tabuleiro para criar o quebra-cabeça."""
    copia_tabuleiro = [linha[:] para linha in tabuleiro]
    celulas_para_remover = 0
    if dificuldade == "facil":
        celulas_para_remover = random.randint(40, 45)
    elif dificuldade == "medio":
        celulas_para_remover = random.randint(46, 53)
    elif dificuldade == "dificil":
        celulas_para_remover = random.randint(54, 60)
    else:
        print("Nível de dificuldade inválido. Usando nível fácil.")
        celulas_para_remover = random.randint(40, 45)

    celulas_removidas = 0
    while celulas_removidas < celulas_para_remover:
        linha = random.randint(0, 8)
        coluna = random.randint(0, 8)
        if copia_tabuleiro[linha][coluna] != 0:
            copia_tabuleiro[linha][coluna] = 0
            celulas_removidas += 1
    return copia_tabuleiro

def gera_sudoku(dificuldade="medio"):
    """Gera um quebra-cabeça de Sudoku com a dificuldade especificada."""
    tabuleiro = gera_tabuleiro_vazio()
    # Preenche o tabuleiro completamente (gera uma solução)
    resolve_sudoku(tabuleiro)
    # Remove algumas células para criar o quebra-cabeça
    return remove_celulas(tabuleiro, dificuldade)

def imprime_tabuleiro(tabuleiro):
    """Imprime o tabuleiro de Sudoku de forma formatada."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(tabuleiro[i][j])
            else:
                print(str(tabuleiro[i][j]) + " ", end="")

if __name__ == "__main__":
    nivel = input("Digite o nível de dificuldade (facil, medio, dificil): ").lower()
    sudoku_gerado = gera_sudoku(nivel)
    print("\nQuebra-cabeça de Sudoku Gerado:")
    imprime_tabuleiro(sudoku_gerado)