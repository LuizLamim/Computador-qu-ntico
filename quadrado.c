#include <stdio.h>

// Função principal do programa
int main() {
    // Declaração de variáveis para armazenar os dois números
    int numero1;
    int numero2;

    // --- Entrada de Dados ---

    // Solicita o primeiro número
    printf("Digite o primeiro número inteiro: ");
    // Lê o primeiro número digitado pelo usuário
    scanf("%d", &numero1);

    // Solicita o segundo número
    printf("Digite o segundo número inteiro: ");
    // Lê o segundo número digitado pelo usuário
    scanf("%d", &numero2);

    // --- Processamento e Saída ---

    // Calcula o quadrado do primeiro número (numero1 * numero1)
    // e exibe o resultado
    printf("\nO quadrado de %d é: %d\n", numero1, numero1 * numero1);

    // Calcula o quadrado do segundo número (numero2 * numero2)
    // e exibe o resultado
    printf("O quadrado de %d é: %d\n", numero2, numero2 * numero2);
