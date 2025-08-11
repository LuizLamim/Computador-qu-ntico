#include <stdio.h>
#include <math.h>

int main() {
    FILE *arquivo;
    double x, y;

    // Abre o arquivo para escrita. Se ele não existir, será criado.
    arquivo = fopen("dados.txt", "w");
    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }

    // Gera os dados para a função y = x^3 no intervalo de -10 a 10
    // O loop incrementa x em 0.1, o que cria 201 pontos para um gráfico suave
    for (x = -10.0; x <= 10.0; x += 0.1) {
        y = pow(x, 3); // A função pow() calcula x^3
        fprintf(arquivo, "%f %f\n", x, y); // Escreve o par (x, y) no arquivo
    }

    // Fecha o arquivo
    fclose(arquivo);

    printf("Dados gerados com sucesso em dados.txt\n");

    return 0;
}