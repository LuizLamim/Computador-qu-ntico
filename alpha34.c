#include <stdio.h>

int main() {
    // Declara um caractere inicial
    char letra = 'A';

    for (int i = 0; i < 5; i++) {
        // Imprime o caractere atual
        printf("%c ", letra);

        letra = letra + 1;
    }

