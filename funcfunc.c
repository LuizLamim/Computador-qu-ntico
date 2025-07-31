#include <stdio.h>
#include <math.h>

// Define a função matemática
double f(double x) {
    return x * cos(x) + sin(x);
}

int main() {
    FILE *fp;
    double x;
    double start = -10.0;
    double end = 10.0;
    double step = 0.05;

    // Abre o arquivo para escrita
    fp = fopen("dados.txt", "w");
    if (fp == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }

    // Calcula e escreve os pontos no arquivo
    for (x = start; x <= end; x += step) {
        fprintf(fp, "%f %f\n", x, f(x));
    }

    // Fecha o arquivo
    fclose(fp);

    printf("Dados gerados em 'dados.txt'. Agora use o gnuplot para criar o gráfico.\n");

    return 0;
}