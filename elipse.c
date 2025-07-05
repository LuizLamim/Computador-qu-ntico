#include <stdio.h>
#include <math.h>

#define PI 3.14159265359

int main() {
    double a, b; // Semi-eixos maior e menor da elipse
    int num_pontos = 100; // Número de pontos para gerar
    double theta; // Ângulo para varrer a elipse

    printf("Digite o comprimento do semi-eixo maior (a): ");
    scanf("%lf", &a);

    printf("Digite o comprimento do semi-eixo menor (b): ");
    scanf("%lf", &b);

    if (a <= 0 || b <= 0) {
        printf("Os semi-eixos devem ser valores positivos.\n");
        return 1; // Saída com erro
    }

    printf("\nPontos da Elipse:\n");
    printf("X\t\tY\n");
    printf("------------------------\n");

    for (int i = 0; i < num_pontos; i++) {
        theta = (double)i / (double)num_pontos * 2 * PI; // Varia de 0 a 2*PI

        double x = a * cos(theta); // Fórmula para o coordenada X
        double y = b * sin(theta); // Fórmula para a coordenada Y

        printf("%.4f\t\t%.4f\n", x, y);
    }

    printf("------------------------\n");
    printf("Para plotar estes pontos, use uma biblioteca gráfica (ex: SDL, OpenGL).\n");

    return 0; // Saída bem-sucedida
}