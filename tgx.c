#include <stdio.h>
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

int main() {
    // Configurações do gráfico
    int largura = 60;        // Largura do terminal em caracteres
    int centro = largura / 2; 
    double passo = 0.1;      // Resolução do eixo X
    double escala_y = 10.0;  // Quão "esticada" a curva será horizontalmente

    printf("Gráfico de tg(x) (Eixo X vertical, Eixo Y horizontal)\n");
    printf("----------------------------------------------------\n");