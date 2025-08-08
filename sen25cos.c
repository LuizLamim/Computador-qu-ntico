#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846
#define NUM_PONTOS 400

int main() {
    FILE *funcao_file = fopen("dados_funcao.txt", "w");
    FILE *constante_file = fopen("dados_constante.txt", "w");

    if (funcao_file == NULL || constante_file == NULL) {
        printf("Erro ao abrir os arquivos.\n");
        return 1;
    }

    double x, y_funcao, y_constante;
    double passo = (4 * PI) / (NUM_PONTOS - 1);

    for (int i = 0; i < NUM_PONTOS; i++) {
        x = -2 * PI + i * passo;
        y_funcao = 3 * sin(x) + 25 * cos(x);
        y_constante = 18.0;

        fprintf(funcao_file, "%f %f\n", x, y_funcao);
        fprintf(constante_file, "%f %f\n", x, y_constante);
    }

    fclose(funcao_file);
    fclose(constante_file);

    printf("Dados gerados com sucesso para os arquivos dados_funcao.txt e dados_constante.txt\n");

    return 0;
}