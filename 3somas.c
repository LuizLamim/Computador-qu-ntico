#include <stdio.h>

int main() {
    // Declaração das variáveis para armazenar os três números e a soma
    int numero1, numero2, numero3, soma;

    // Solicita ao usuário que insira o primeiro número
    printf("Digite o primeiro numero inteiro: ");
    // Lê o primeiro número digitado e armazena em 'numero1'
    scanf("%d", &numero1);

    // Solicita ao usuário que insira o segundo número
    printf("Digite o segundo numero inteiro: ");
    // Lê o segundo número digitado e armazena em 'numero2'
    scanf("%d", &numero2);

    // Solicita ao usuário que insira o terceiro número
    printf("Digite o terceiro numero inteiro: ");
    // Lê o terceiro número digitado e armazena em 'numero3'
    scanf("%d", &numero3);

    // Realiza a operação de soma
    soma = numero1 + numero2 + numero3;

    // Exibe o resultado da soma
    printf("\n"); // Adiciona uma linha em branco para melhor formatação
    printf("A soma dos tres numeros e: %d\n", soma);

    // Retorna 0 para indicar que o programa foi executado com sucesso
    return 0;
}