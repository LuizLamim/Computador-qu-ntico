#include <stdio.h> // Inclui a biblioteca padrão de entrada e saída

int main() {
    // Declaração e inicialização dos vetores unitários
    // Vetor unitário na direção X
    double vetor1[3] = {1.0, 0.0, 0.0}; 
    // Vetor unitário na direção Y
    double vetor2[3] = {0.0, 1.0, 0.0}; 

    // Imprime o primeiro vetor unitário
    printf("Primeiro vetor unitário: (%.1f, %.1f, %.1f)\n", vetor1[0], vetor1[1], vetor1[2]);

    // Imprime o segundo vetor unitário
    printf("Segundo vetor unitário: (%.1f, %.1f, %.1f)\n", vetor2[0], vetor2[1], vetor2[2]);

    return 0; // Indica que o programa foi executado com sucesso
}