#include <stdio.h>
#include <math.h> 

#define PI 3.14159265358979323846
#define NUM_POINTS 400

int main() {
    FILE *fp;
    double x, y;
    double start = -2 * PI;
    double end = 2 * PI;
    double step = (end - start) / NUM_POINTS;

    fp = fopen("secante_data.txt", "w");
    if (fp == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }

    for (int i = 0; i < NUM_POINTS; i++) {
        x = start + i * step;

        // Evitar pontos próximos às assíntotas para evitar divisão por zero
        // cos(x) é zero em PI/2 + n*PI
        if (fabs(cos(x)) > 1e-6) { // Usamos um pequeno epsilon para evitar valores muito próximos de zero
            y = 1.0 / cos(x);
            fprintf(fp, "%.6f %.6f\n", x, y); // Escreve x e y no arquivo
        }
    }

    fclose(fp);
    printf("Dados da função secante gerados em 'secante_data.txt'\n");


    return 0;
}