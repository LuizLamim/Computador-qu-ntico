#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265358979323846

void create_data_files() {
    FILE *fp_seno, *fp_cosseno, *fp_tangente;
    double x;

    // Abrir arquivos para escrita
    fp_seno = fopen("seno.dat", "w");
    fp_cosseno = fopen("cosseno.dat", "w");
    fp_tangente = fopen("tangente.dat", "w");

    if (fp_seno == NULL || fp_cosseno == NULL || fp_tangente == NULL) {
        printf("Erro ao criar os arquivos de dados.\n");
        exit(1);
    }

    // Gerar e salvar os dados
    for (x = -2 * PI; x <= 2 * PI; x += 0.05) {
        fprintf(fp_seno, "%f %f\n", x, sin(x));
        fprintf(fp_cosseno, "%f %f\n", x, cos(x));
        // A tangente tem descontinuidades, vamos plotar apenas em pontos válidos
        if (fabs(cos(x)) > 1e-6) {
            fprintf(fp_tangente, "%f %f\n", x, tan(x));
        }
    }

    // Fechar os arquivos
    fclose(fp_seno);
    fclose(fp_cosseno);
    fclose(fp_tangente);

    printf("Arquivos de dados criados com sucesso.\n");
}

void create_gnuplot_script() {
    FILE *fp_script;

    fp_script = fopen("plot_functions.gp", "w");

    if (fp_script == NULL) {
        printf("Erro ao criar o script do gnuplot.\n");
        exit(1);
    }

    // Escrever os comandos do gnuplot no arquivo
    fprintf(fp_script, "set terminal pngcairo enhanced font 'arial,12'\n");
    fprintf(fp_script, "set output 'functions.png'\n");
    fprintf(fp_script, "set title 'Funcoes Trigonometricas'\n");
    fprintf(fp_script, "set xlabel 'x'\n");
    fprintf(fp_script, "set ylabel 'y'\n");
    fprintf(fp_script, "set grid\n");
    fprintf(fp_script, "set xrange [-7:7]\n");
    fprintf(fp_script, "set yrange [-5:5]\n");
    fprintf(fp_script, "set key top left\n");
    fprintf(fp_script, "plot 'seno.dat' with lines title 'sin(x)', \\\n");
    fprintf(fp_script, "'cosseno.dat' with lines title 'cos(x)', \\\n");
    fprintf(fp_script, "'tangente.dat' with lines title 'tan(x)'\n");

    fclose(fp_script);

    printf("Script do gnuplot criado com sucesso.\n");
}

int main() {
    // 1. Criar os arquivos com os dados
    create_data_files();

    // 2. Criar o script para o gnuplot
    create_gnuplot_script();

    // 3. Executar o gnuplot
    printf("Executando o gnuplot...\n");
    system("gnuplot plot_functions.gp");

    printf("Plotagem concluída. O gráfico foi salvo em 'functions.png'.\n");

    return 0;
}