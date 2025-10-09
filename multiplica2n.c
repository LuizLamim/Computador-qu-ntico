#include <stdio.h>

int main() {
    // Declara as variáveis para armazenar os dois números e o resultado
    int num1, num2, resultado;

    // Pede ao usuário para digitar o primeiro número
    printf("Digite o primeiro número: ");
    // Lê o primeiro número digitado e armazena em num1
    scanf("%d", &num1);

    // Pede ao usuário para digitar o segundo número
    printf("Digite o segundo número: ");
    // Lê o segundo número digitado e armazena em num2
    scanf("%d", &num2);

    // Realiza a multiplicação e armazena o valor em 'resultado'
    resultado = num1 * num2;

    // Imprime o resultado formatado
    printf("A multiplicação de %d por %d é: %d\n", num1, num2, resultado);

    // Indica que o programa terminou com sucesso
    return 0;
}