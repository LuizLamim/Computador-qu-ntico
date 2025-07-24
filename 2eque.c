#include <stdio.h>
#include <stdlib.h> // Para system()

int main() {
    FILE *fp1, *fp2, *gp_script;
    double x;

    // Abrir arquivos para armazenar os dados das funções
    fp1 = fopen("data_func1.txt", "w");
    fp2 = fopen("data_func2.txt", "w");

    if (fp1 == NULL || fp2 == NULL) {
        printf("Erro ao abrir os arquivos de dados.\n");
        return 1;
    }

    // Gerar dados para a primeira função: y = 3x + 3
    for (x = -10.0; x <= 10.0; x += 0.1) { // Incremento de 0.1 para mais pontos
        fprintf(fp1, "%lf %lf\n", x, 3 * x + 3);
    }
    fclose(fp1);

    // Gerar dados para a segunda função: y = -3x + 3
    for (x = -10.0; x <= 10.0; x += 0.1) {
        fprintf(fp2, "%lf %lf\n", x, -3 * x + 3);
    }
    fclose(fp2);

    // Criar um script Gnuplot para plotar os dados
    gp_script = fopen("plot.gp", "w");
    if (gp_script == NULL) {
        printf("Erro ao criar o script Gnuplot.\n");
        return 1;
    }

    fprintf(gp_script, "set title 'Gráfico das Funções y = 3x + 3 e y = -3x + 3'\n");
    fprintf(gp_script, "set xlabel 'Eixo X'\n");
    fprintf(gp_script, "set ylabel 'Eixo Y'\n");
    fprintf(gp_script, "set grid\n");
    fprintf(gp_script, "set xzeroaxis\n"); // Desenha o eixo X
    fprintf(gp_script, "set yzeroaxis\n"); // Desenha o eixo Y
    fprintf(gp_script, "plot 'data_func1.txt' with lines title 'y = 3x + 3' lc rgb 'blue', \\\n");
    fprintf(gp_script, "     'data_func2.txt' with lines title 'y = -3x + 3' lc rgb 'red' dt 2\n"); // dt 2 = dashed line

    fclose(gp_script);

    // Chamar o Gnuplot para executar o script
    // No Windows, pode ser necessário 'start gnuplot -persist plot.gp'
    // No Linux/macOS: 'gnuplot -persist plot.gp'
    #ifdef _WIN32
        system("start gnuplot -persist plot.gp"); // -persist mantém a janela aberta
    #else
        system("gnuplot -persist plot.gp"); // -persist mantém a janela aberta
    #endif


    printf("Dados gerados e Gnuplot invocado. Verifique a janela do Gnuplot.\n");

    return 0;
}