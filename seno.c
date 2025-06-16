#include <stdio.h>
#include <math.h> // Para a função sin()

#define PI 3.14159265358979323846

int main() {
    FILE *fp;
    double x, y;
    int num_pontos = 1000; // Número de pontos para suavizar o gráfico
    double inicio = 0.0;
    double fim = 2.0 * PI; // Plotar de 0 a 2*PI

    // Abrir o arquivo para escrita
    fp = fopen("dados_seno.txt", "w");
    if (fp == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }

    // Gerar os pontos e escrever no arquivo
    for (int i = 0; i < num_pontos; i++) {
        x = inicio + (fim - inicio) * i / (num_pontos - 1);
        y = sin(x);
        fprintf(fp, "%lf %lf\n", x, y); // Escreve x e y separados por espaço, seguidos de nova linha
    }

    // Fechar o arquivo
    fclose(fp);

    printf("Dados do seno gerados em 'dados_seno.txt'\n");

    return 0;
}