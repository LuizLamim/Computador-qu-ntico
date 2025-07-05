#include <stdio.h>
#include <math.h>

#define PI 3.14159265359

int main() {
    double raio; // Raio do círculo
    int num_pontos = 100; // Número de pontos para gerar
    double theta; // Ângulo para varrer o círculo

    printf("Digite o raio do círculo: ");
    scanf("%lf", &raio);

    if (raio <= 0) {
        printf("O raio deve ser um valor positivo.\n");
        return 1; // Saída com erro
    }

    printf("\nPontos do Círculo:\n");
    printf("X\t\tY\n");
    printf("------------------------\n");

    for (int i = 0; i < num_pontos; i++) {
        theta = (double)i / (double)num_pontos * 2 * PI; // Varia de 0 a 2*PI

        double x = raio * cos(theta); // Fórmula para a coordenada X
        double y = raio * sin(theta); // Fórmula para a coordenada Y

        printf("%.4f\t\t%.4f\n", x, y);
    }

    printf("------------------------\n");
    printf("Para plotar estes pontos, use uma biblioteca gráfica (ex: SDL, OpenGL).\n");

    return 0; // Saída bem-sucedida
}