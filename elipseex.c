#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NUM_PONTOS 1000
#define PI 3.14159265358979323846

int main() {
    // Definindo os semi-eixos para uma elipse com alta excentricidade
    // Excentricidade (e) = sqrt(1 - (b^2 / a^2))
    // Quando 'b' é muito menor que 'a', 'e' se aproxima de 1.
    double a = 5.0; // Semi-eixo maior
    double b = 1.0; // Semi-eixo menor

    // Calculando a excentricidade
    double excentricidade = sqrt(1.0 - (b * b) / (a * a));

    // Abrindo um arquivo para salvar os pontos da elipse
    FILE *fp = fopen("dados_elipse.txt", "w");
    if (fp == NULL) {
        perror("Erro ao abrir o arquivo");
        return 1;
    }

    // Gerando os pontos da elipse
    for (int i = 0; i <= NUM_PONTOS; i++) {
        double theta = (double)i / NUM_PONTOS * 2.0 * PI;
        double x = a * cos(theta);
        double y = b * sin(theta);
        fprintf(fp, "%.4f %.4f\n", x, y);
    }

    // Fechando o arquivo
    fclose(fp);

    printf("Pontos da elipse salvos em dados_elipse.txt\n");
    printf("Gerando o gráfico com Gnuplot...\n");

    // Abrindo um pipe para o Gnuplot e enviando os comandos
    FILE *gnuplotPipe = popen("gnuplot -persistent", "w");
    if (gnuplotPipe == NULL) {
        perror("Erro ao abrir pipe para o Gnuplot");
        return 1;
    }

    // Enviando os comandos de plotagem para o Gnuplot
    fprintf(gnuplotPipe, "set title 'Gráfico de uma Elipse com Excentricidade Alta (e = %.2f)'\n", excentricidade);
    fprintf(gnuplotPipe, "set xlabel 'Eixo X'\n");
    fprintf(gnuplotPipe, "set ylabel 'Eixo Y'\n");
    fprintf(gnuplotPipe, "set size ratio -1\n"); // Força a proporção 1:1 para evitar distorção
    fprintf(gnuplotPipe, "plot 'dados_elipse.txt' with lines notitle\n");
    
    // Fechando o pipe
    pclose(gnuplotPipe);

    return 0;
}