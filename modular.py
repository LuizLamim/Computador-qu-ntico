#include <stdio.h>
#include <math.h>

#define WIDTH 60  // Largura do gráfico
#define HEIGHT 20 // Altura do gráfico

int main() {
    // A função f(x) = |x^2| é a mesma que f(x) = x^2 para números reais.
    // O gráfico será uma parábola simples.

    // A matriz (grid) que representará o nosso gráfico
    char grid[HEIGHT][WIDTH];

    // Escalas para mapear coordenadas matemáticas para a matriz
    double scale_x = (double)WIDTH / 10.0;
    double scale_y = (double)HEIGHT / 25.0;

    // Preenchendo a matriz com espaços em branco
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            grid[i][j] = ' ';
        }
    }

    // Desenhando os eixos x e y
    int origin_x = WIDTH / 2;
    int origin_y = HEIGHT;

    // Eixo Y
    for (int i = 0; i < HEIGHT; i++) {
        grid[i][origin_x] = '|';
    }

    // Eixo X
    for (int j = 0; j < WIDTH; j++) {
        grid[origin_y - 1][j] = '-';
    }
    
    // Origem
    grid[origin_y - 1][origin_x] = '+';

    // Plotando os pontos da função
    // Vamos de -5 a 5 com um passo pequeno para cobrir a largura do gráfico
    for (double x = -5.0; x <= 5.0; x += 0.1) {
        double y = x * x;

        // Convertendo as coordenadas matemáticas (x, y) para coordenadas da matriz
        int plot_x = (int)(x * scale_x + origin_x);
        int plot_y = (int)(origin_y - y * scale_y - 1);

        // Verificando se o ponto está dentro dos limites da matriz
        if (plot_x >= 0 && plot_x < WIDTH && plot_y >= 0 && plot_y < HEIGHT) {
            grid[plot_y][plot_x] = '*';
        }
    }

    // Imprimindo a matriz na tela para exibir o gráfico
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            printf("%c", grid[i][j]);
        }
        printf("\n");
    }

    return 0;
}