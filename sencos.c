#include <stdio.h>
#include <math.h> // Para sin() e cos()

#define PI 3.14159265358979323846 // Definindo PI
#define NUM_POINTS 1000          // Número de pontos para suavizar o gráfico

int main() {
    FILE *data_file;
    FILE *gnuplot_script_file;
    double x, y;
    double x_start = -2 * PI;
    double x_end = 2 * PI;
    double step = (x_end - x_start) / NUM_POINTS;

    // 1. Gerar os dados e salvar em um arquivo (data.dat)
    data_file = fopen("data.dat", "w"); // Abre o arquivo para escrita
    if (data_file == NULL) {
        perror("Erro ao abrir data.dat");
        return 1;
    }

    for (int i = 0; i <= NUM_POINTS; i++) {
        x = x_start + i * step;
        y = sin(x) + cos(x);
        fprintf(data_file, "%.5f %.5f\n", x, y); // Escreve x e y no arquivo
    }
    fclose(data_file); // Fecha o arquivo de dados

    // 2. Criar um script para o Gnuplot (plot.gp)
    gnuplot_script_file = fopen("plot.gp", "w"); // Abre o arquivo para escrita
    if (gnuplot_script_file == NULL) {
        perror("Erro ao abrir plot.gp");
        return 1;
    }

    fprintf(gnuplot_script_file, "set title 'Gráfico da Função sen(x) + cos(x)'\n");
    fprintf(gnuplot_script_file, "set xlabel 'x'\n");
    fprintf(gnuplot_script_file, "set ylabel 'y'\n");
    fprintf(gnuplot_script_file, "set grid\n");
    fprintf(gnuplot_script_file, "set xzeroaxis lt -1 lc rgb 'black'\n"); // Eixo X em 0
    fprintf(gnuplot_script_file, "set yzeroaxis lt -1 lc rgb 'black'\n"); // Eixo Y em 0
    fprintf(gnuplot_script_file, "plot 'data.dat' using 1:2 with lines title 'sen(x) + cos(x)' lc rgb 'blue'\n");
    // 'data.dat': arquivo de dados
    // using 1:2: usa a primeira coluna para X e a segunda para Y
    // with lines: plota como uma linha
    // title: título da linha na legenda
    // lc rgb 'blue': cor da linha (line color rgb blue)

    fclose(gnuplot_script_file); // Fecha o arquivo do script Gnuplot

    // 3. Informar o usuário como plotar
    printf("Dados salvos em 'data.dat'.\n");
    printf("Script Gnuplot salvo em 'plot.gp'.\n");
    printf("Para plotar, abra um terminal e execute:\n");
    printf("gnuplot plot.gp -persist\n"); // -persist mantém a janela aberta
    printf("Ou apenas:\n");
    printf("gnuplot\n");
    printf("plot 'data.dat' using 1:2 with lines title 'sen(x) + cos(x)' lc rgb 'blue'\n");

    return 0;
}