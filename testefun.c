#include <stdio.h>
#include <math.h>

#define FILENAME "dados_cos.dat"
#define X_MIN -10.0
#define X_MAX 10.0
#define STEP 0.1

int main() {
    FILE *fp;
    double x, y;

    // Abrir o arquivo para escrita
    fp = fopen(FILENAME, "w");
    if (fp == NULL) {
        printf("Erro ao abrir o arquivo %s\n", FILENAME);
        return 1;
    }

// Gerar os dados da função cos(x) + 10 e escrever no arquivo
    for (x = X_MIN; x <= X_MAX; x += STEP) {
        y = cos(x) + 10;
        fprintf(fp, "%f %f\n", x, y);
    }

    // Fechar o arquivo
    fclose(fp);

    printf("Dados da função cos(x) + 10 gerados com sucesso no arquivo %s\n", FILENAME);
    printf("Agora, use o GNUPlot para plotar o gráfico.\n");
    
    return 0;
}