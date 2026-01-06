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

    for (double x = -M_PI; x <= M_PI; x += passo) {
        double y = tan(x);

        // Mapeia o valor da tangente para uma coluna no terminal
        // O '+ 0.5' serve para arredondamento
        int pos = (int)(centro + (y * escala_y) + 0.5);

        printf("%5.2f |", x); // Imprime o valor de X

        // Verifica se a posição cabe na tela (filtra os infinitos/assíntotas)
        if (pos >= 0 && pos < largura) {
            // Imprime espaços até a posição do ponto
            for (int i = 0; i < pos; i++) {
                printf(" ");
            }
            printf("*\n"); // O ponto do gráfico
        } else {
            // Se o valor for muito alto (assíntota), indica com seta
            if (y > 0) printf("  ---> +Infinito\n");
            else       printf("  <--- -Infinito\n");
        }
    }