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