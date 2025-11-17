#include <stdio.h>

int main() {
    int numeros_pares[] = {2, 4, 6, 8};
    int total_numeros = sizeof(numeros_pares) / sizeof(numeros_pares[0]);
    int i, j;

    printf("--- Plotagem Simples dos 4 Primeiros Números Pares ---\n");
    printf("(Cada '*' representa uma unidade)\n\n");

    for (i = 0; i < total_numeros; i++) {
        int valor = numeros_pares[i];

        // Imprime o índice (eixo Y) e o valor
        printf("P%d (%d): ", i + 1, valor);

        // Loop interno para "plotar" o número com asteriscos (eixo X)
        for (j = 0; j < valor; j++) {
            printf("*");
        }

        // Nova linha para o próximo número
        printf("\n");
    }

    printf("\n------------------------------------------------------\n");

    return 0; // Retorna 0 para indicar que o programa foi executado com sucesso
}