#include <stdio.h> // Para entrada e saída (printf, scanf)
#include <math.h>  // Para funções matemáticas (sqrt)
#include <stdlib.h> // Para a função exit()

int main() {
    int opcao;
    double a, b, c, excentricidade;

    printf("--- Calculadora de Excentricidade de Elipse ---\n");
    printf("Selecione a opcao de entrada de dados:\n");
    printf("1. Semieixo maior (a) e Semieixo menor (b)\n");
    printf("2. Semieixo maior (a) e Distancia focal (c)\n");

    while (1) { // Loop infinito para garantir uma entrada válida
        printf("Digite 1 ou 2: ");
        if (scanf("%d", &opcao) == 1 && (opcao == 1 || opcao == 2)) {
            break; // Sai do loop se a entrada for válida
        } else {
            printf("Opcao invalida. Por favor, digite 1 ou 2.\n");
            // Limpa o buffer de entrada para evitar loops infinitos com entradas inválidas
            while (getchar() != '\n');
        }
    }

    if (opcao == 1) {
        printf("Digite o valor do semieixo maior (a): ");
        while (scanf("%lf", &a) != 1 || a <= 0) {
            printf("Valor invalido. Digite um numero positivo para 'a': ");
            while (getchar() != '\n');
        }

        printf("Digite o valor do semieixo menor (b): ");
        while (scanf("%lf", &b) != 1 || b <= 0) {
            printf("Valor invalido. Digite um numero positivo para 'b': ");
            while (getchar() != '\n');
        }

        if (b >= a) {
            printf("Erro: O semieixo menor (b) deve ser menor que o semieixo maior (a) para uma elipse.\n");
            return 1; // Retorna com erro
        }

        c = sqrt(a*a - b*b);
        excentricidade = c / a;

    } else { // opcao == 2
        printf("Digite o valor do semieixo maior (a): ");
        while (scanf("%lf", &a) != 1 || a <= 0) {
            printf("Valor invalido. Digite um numero positivo para 'a': ");
            while (getchar() != '\n');
        }

        printf("Digite o valor da distancia focal (c): ");
        while (scanf("%lf", &c) != 1 || c < 0) {
            printf("Valor invalido. Digite um numero nao negativo para 'c': ");
            while (getchar() != '\n');
        }

        if (c >= a) {
            printf("Erro: A distancia focal (c) deve ser menor que o semieixo maior (a) para uma elipse.\n");
            return 1; // Retorna com erro
        }

        excentricidade = c / a;
    }

    printf("\nO semieixo maior (a) e: %.4lf\n", a);
    if (opcao == 1) {
        printf("O semieixo menor (b) e: %.4lf\n", b);
        printf("A distancia focal (c) calculada e: %.4lf\n", c);
    } else {
        printf("A distancia focal (c) e: %.4lf\n", c);
    }

    printf("\nA excentricidade da elipse e: %.4lf\n", excentricidade);

    return 0; // Indica que o programa executou com sucesso
}