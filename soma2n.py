#include <stdio.h>

int main() {
    // Declaração das variáveis para os dois números e o resultado
    int numero1, numero2, soma;

    // Solicita o primeiro número ao usuário
    printf("Digite o primeiro número inteiro: ");
    // Lê o primeiro número e armazena na variável numero1
    scanf("%d", &numero1);

    // Solicita o segundo número ao usuário
    printf("Digite o segundo número inteiro: ");
    // Lê o segundo número e armazena na variável numero2
    scanf("%d", &numero2);

    // Realiza a soma
    soma = numero1 + numero2;

    // Exibe o resultado da soma
    printf("\nA soma de %d e %d é: %d\n", numero1, numero2, soma);