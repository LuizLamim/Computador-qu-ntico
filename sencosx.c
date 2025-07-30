#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846
#define NUM_POINTS 400

int main() {
    double x, y;
    double start_x = -2 * PI;
    double end_x = 2 * PI;
    double step = (end_x - start_x) / (NUM_POINTS - 1);

    printf("# x, y\n"); // Cabeçalho para identificar as colunas

    for (int i = 0; i < NUM_POINTS; i++) {
        x = start_x + i * step;
        y = sin(x) + 35 * cos(x);
        printf("%lf, %lf\n", x, y);
    }

    return 0;
}