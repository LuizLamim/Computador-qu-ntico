#include <stdio.h> // Para funções de entrada e saída (printf, scanf)

int main() {
    // 1. Criando uma matriz 3x3 com valores predefinidos
    int matriz1[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    printf("Matriz 1:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", matriz1[i][j]);
        }
        printf("\n"); // Quebra de linha após cada linha da matriz
    }

    // ---

    // 2. Criando uma matriz 3x3 preenchida com zeros
    int matriz2[3][3] = {0}; // Inicializa todos os elementos com zero

    printf("\nMatriz 2 (preenchida com zeros):\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", matriz2[i][j]);
        }
        printf("\n");
    }

    // ---

    // 3. Criando uma matriz 3x3 com entrada do usuário
    int matriz3[3][3];

    printf("\nDigite os elementos da matriz 3x3 (9 numeros inteiros):\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("Elemento [%d][%d]: ", i, j);
            scanf("%d", &matriz3[i][j]); // Lê o valor do usuário e armazena
        }
    }

    printf("\nMatriz 3 (criada pelo usuario):\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", matriz3[i][j]);
        }
        printf("\n");
    }

    return 0; // Indica que o programa foi executado com sucesso
}