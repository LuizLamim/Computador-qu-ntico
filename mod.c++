#include <iostream>
#include <cmath>
#include <cstdio>

int main() {
    // Abre um pipe para o gnuplot
    FILE* gnuplotPipe = popen("gnuplot -persistent", "w");
    if (!gnuplotPipe) {
        std::cerr << "Erro: Não foi possível abrir o pipe para o gnuplot." << std::endl;
        return 1;
    }

    // Configurações do gráfico
    fprintf(gnuplotPipe, "set title 'Grafico de | sen(x) + 10 |'\n");
    fprintf(gnuplotPipe, "set xlabel 'x'\n");
    fprintf(gnuplotPipe, "set ylabel 'y'\n");
    fprintf(gnuplotPipe, "set grid\n");
    fprintf(gnuplotPipe, "plot '-' with lines title '| sen(x) + 10 |'\n");

    // Loop para calcular e enviar os pontos para o gnuplot
    const double PI = 3.14159265358979323846;
    const double startX = -10.0;
    const double endX = 10.0;
    const double step = 0.01;

    for (double x = startX; x <= endX; x += step) {
        double y = std::abs(std::sin(x) + 10);
        fprintf(gnuplotPipe, "%f %f\n", x, y);
    }

    // Encerra o envio de dados
    fprintf(gnuplotPipe, "e\n");

    // Fecha o pipe
    fflush(gnuplotPipe);
    pclose(gnuplotPipe);

    std::cout << "Gráfico gerado com sucesso!" << std::endl;

    return 0;
}