#include <stdio.h>
#include <math.h>

// Define a função f(x)
double f(double x) {
    return 13 * cos(x);
}

int main() {
    // Define o intervalo de x para o cálculo (de -2*pi a 2*pi)
    double inicio_x = -2 * M_PI;
    double fim_x = 2 * M_PI;

    // Define o número de pontos a serem calculados (para maior precisão)
    int num_pontos = 1000;

    // Calcula o passo entre cada ponto
    double passo = (fim_x - inicio_x) / (num_pontos - 1);

    printf("x, f(x)\n"); // Cabeçalho para o CSV

    // Loop para calcular e imprimir os valores
    for (int i = 0; i < num_pontos; i++) {
        double x = inicio_x + i * passo;
        double y = f(x);
        printf("%f, %f\n", x, y);
    }

    return 0;
}