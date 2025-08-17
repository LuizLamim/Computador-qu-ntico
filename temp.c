#include <stdio.h>

int main() {
    int quantidade, i;
    float temperatura, soma_temperaturas = 0.0, media_temperaturas;

    // Pede ao usuário a quantidade de temperaturas a serem inseridas
    printf("Quantas temperaturas voce quer inserir para calcular a media? ");
    scanf("%d", &quantidade);

    // Valida se a quantidade é positiva
    if (quantidade <= 0) {
        printf("Por favor, digite um numero maior que zero.\n");
        return 1; // Retorna um código de erro
    }

    // Loop para ler as temperaturas e somá-las
    for (i = 1; i <= quantidade; i++) {
        printf("Digite a temperatura %d: ", i);
        scanf("%f", &temperatura);
        soma_temperaturas += temperatura;
    }

    // Calcula a media
    media_temperaturas = soma_temperaturas / quantidade;

    // Exibe os resultados
    printf("\nA soma total das temperaturas e: %.2f C\n", soma_temperaturas);
    printf("A media das temperaturas e: %.2f C\n", media_temperaturas);

    return 0; // Retorna 0 para indicar sucesso
}