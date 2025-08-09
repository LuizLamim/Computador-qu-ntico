#include <stdio.h>
#include <math.h>

// A função que queremos plotar
double f(double x) {
    return exp(x) + 3 * x;
}

int main() {
    FILE *fp;
    double x;
    double start = -5.0; // Início do intervalo
    double end = 5.0;    // Fim do intervalo
    double step = 0.1;   // Passo para cada ponto

    // Abre o arquivo para escrita
    fp = fopen("dados.dat", "w");
    if (fp == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }

    // Calcula os valores e escreve no arquivo
    for (x = start; x <= end; x += step) {
        fprintf(fp, "%lf %lf\n", x, f(x));
    }

    // Fecha o arquivo
    fclose(fp);

    printf("Dados da função salvos em 'dados.dat'.\n");

    return 0;
}