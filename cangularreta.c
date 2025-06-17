#include <stdio.h>

int main() {
    double x1, y1, x2, y2;
    double coeficiente_angular;

    // Solicita as coordenadas do primeiro ponto
    printf("Digite as coordenadas do primeiro ponto (x1 y1): ");
    scanf("%lf %lf", &x1, &y1);

    // Solicita as coordenadas do segundo ponto
    printf("Digite as coordenadas do segundo ponto (x2 y2): ");
    scanf("%lf %lf", &x2, &y2);

    // Verifica se os pontos têm o mesmo x, o que resultaria em uma divisão por zero
    if (x2 - x1 == 0) {
        printf("Erro: A reta é vertical. O coeficiente angular é indefinido.\n");
    } else {
        // Calcula o coeficiente angular
        coeficiente_angular = (y2 - y1) / (x2 - x1);
        printf("O coeficiente angular da reta e: %.2lf\n", coeficiente_angular);
    }

    return 0;
}