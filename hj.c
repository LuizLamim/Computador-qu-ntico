#include <stdio.h>

int main() {
    // 1. Declaração das variáveis
    int numero1, numero2, resultado;

    // 2. Solicita o primeiro número
    printf("Digite o primeiro número: ");
    scanf("%d", &numero1);

    // 3. Solicita o segundo número
    printf("Digite o segundo número: ");
    scanf("%d", &numero2);

    resultado = numero1 + numero2;

    printf("A soma de %d + %d é igual a: %d\n", numero1, numero2, resultado);

    return 0;
}