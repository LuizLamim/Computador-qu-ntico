#include <stdio.h>
#include <math.h> // Para a função sin()

int main() {
    FILE *fp;
    double x, y;
    double start_x = -2 * M_PI; // -2*pi
    double end_x = 2 * M_PI;    // 2*pi
    int num_points = 400;
    double step = (end_x - start_x) / (num_points - 1);

    // 1. Abrir um arquivo para escrever os dados
    fp = fopen("dados_seno.dat", "w");
    if (fp == NULL) {
        perror("Erro ao abrir o arquivo");
        return 1;
    }

    // 2. Gerar e escrever os valores de x e y no arquivo
    for (int i = 0; i < num_points; i++) {
        x = start_x + i * step;
        y = sin(x) + 3;
        fprintf(fp, "%lf %lf\n", x, y); // Escreve x e y separados por espaço
    }

    // 3. Fechar o arquivo
    fclose(fp);

    // 4. Chamar o Gnuplot para plotar os dados do arquivo
    //    Este comando será executado pelo sistema operacional.
    //    Você precisa ter o Gnuplot instalado e no seu PATH.
    system("gnuplot -persist -e \"plot 'dados_seno.dat' using 1:2 with lines title 'y = sen(x) + 3'\"");

    printf("Dados gerados em 'dados_seno.dat' e Gnuplot chamado.\n");

    return 0;
}