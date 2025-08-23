#include <stdio.h>
#include <math.h>

int main() {
    FILE *arquivo;
    double x, y;
    int i;
    int num_pontos = 100;
    double inicio = 0.1;
    double fim = 10.0;
    double passo = (fim - inicio) / (num_pontos - 1);

    // Abre o arquivo para escrita
    arquivo = fopen("dados.dat", "w");
    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        return 1;
    }

    // Calcula os valores da função e escreve no arquivo
    for (i = 0; i < num_pontos; i++) {
        x = inicio + i * passo;
        y = log10(x) + 10.0;
        fprintf(arquivo, "%f %f\n", x, y);
    }

    // Fecha o arquivo
    fclose(arquivo);

    printf("Dados da função salvos em 'dados.dat'.\n");

    return 0;
}