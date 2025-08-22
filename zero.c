#include <stdio.h>

int main() {
    // Declara e inicializa a matriz 4x4 com zeros
    int matriz[4][4] = {0};

    // Imprime a matriz
    printf("Matriz 4x4 de Zeros:\n");
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%d ", matriz[i][j]);
        }
        printf("\n"); // Nova linha para a próxima linha da matriz
    }

    return 0;
}