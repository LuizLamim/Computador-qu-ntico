#include <stdio.h>

int main() {
    int matriz_nula[3][3] = {0};

    int linhas = 3;
    int colunas = 3;

    printf("Matriz Nula 3x3:\n");
    
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            printf("%d ", matriz_nula[i][j]);
        }
        printf("\n");
    }

    return 0;
}
