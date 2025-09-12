#include <stdio.h>
#include <math.h>

int main() {
    // Abre o arquivo para escrita. 'w' significa write.
    FILE *fp = fopen("dados.dat", "w");

    // Verifica se o arquivo foi aberto com sucesso.
    if (fp == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }

    double x, y;

    // Loop para calcular os valores da função no intervalo [-10, 10]
    for (x = -10.0; x <= 10.0; x += 0.1) {
        // Calcula a função f(x) = sin(x) + 35x
        y = sin(x) + 35 * x;

        // Escreve os valores de x e y no arquivo.
        // O formato "%.2f %.2f\n" garante duas casas decimais e uma nova linha.
        fprintf(fp, "%.2f %.2f\n", x, y);
    }