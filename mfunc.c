#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265358979323846
#define NUM_POINTS 500

// Função que queremos plotar
double f(double x) {
    return fabs(sin(x) + cos(x));
}

int main() {
    // Abre um arquivo para salvar os dados
    FILE *data_file = fopen("function_data.dat", "w");
    if (data_file == NULL) {
        perror("Erro ao abrir o arquivo de dados");
        return 1;
    }

    // Gera os pontos da função e salva no arquivo
    double x, y;
    double start = -2 * PI;
    double end = 2 * PI;
    double step = (end - start) / (NUM_POINTS - 1);

    for (int i = 0; i < NUM_POINTS; i++) {
        x = start + i * step;
        y = f(x);
        fprintf(data_file, "%f %f\n", x, y);
    }

    fclose(data_file);

    // Usa o popen para enviar comandos ao GNUPlot
    FILE *gnuplot_pipe = popen("gnuplot -persistent", "w");
    if (gnuplot_pipe == NULL) {
        perror("Erro ao abrir o pipe para o gnuplot");
        return 1;
    }

    fprintf(gnuplot_pipe, "set title 'Gráfico da função f(x) = |sin(x) + cos(x)|'\n");
    fprintf(gnuplot_pipe, "set xlabel 'x'\n");
    fprintf(gnuplot_pipe, "set ylabel 'f(x)'\n");
    fprintf(gnuplot_pipe, "set grid\n");
    fprintf(gnuplot_pipe, "plot 'function_data.dat' with lines title '|sin(x) + cos(x)|'\n");
    fprintf(gnuplot_pipe, "pause mouse close\n"); // Espera por uma ação do mouse para fechar
    
    pclose(gnuplot_pipe);

    return 0;
}