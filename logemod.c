#include <stdio.h>
#include <math.h>

// A função que vamos plotar
double f(double x) {
    return fabs(log(x));
}

int main() {
    FILE *arquivo;
    double x;
    int i;
    int num_pontos = 400;
    double inicio = 0.01;
    double fim = 10.0;
    double passo = (fim - inicio) / num_pontos;

    // Abre o arquivo para escrita
    arquivo = fopen("dados.dat", "w");
    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }

    // Calcula e escreve os pontos no arquivo
    for (i = 0; i < num_pontos; i++) {
        x = inicio + i * passo;
        // Não permite x ser 0, pois log(0) é indefinido
        if (x > 0) {
            fprintf(arquivo, "%.4f %.4f\n", x, f(x));
        }
    }

    // Fecha o arquivo
    fclose(arquivo);
    printf("Dados gerados em 'dados.dat' com sucesso!\n");

    return 0;
}