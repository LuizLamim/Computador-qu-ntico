#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

const double PI = 3.14159265358979323846;
const int NUM_POINTS = 500;

// Função que queremos plotar
double f(double x) {
    return std::abs(std::sin(x) + std::cos(x));
}

int main() {
    // 1. Gera os dados e salva em um arquivo
    std::ofstream dataFile("function_data.dat");
    if (!dataFile.is_open()) {
        std::cerr << "Erro ao abrir o arquivo de dados!" << std::endl;
        return 1;
    }

    double start = -2 * PI;
    double end = 2 * PI;
    double step = (end - start) / (NUM_POINTS - 1);

    for (int i = 0; i < NUM_POINTS; ++i) {
        double x = start + i * step;
        double y = f(x);
        dataFile << x << " " << y << std::endl;
    }

    dataFile.close();

    // 2. Envia comandos ao GNUPlot para plotar o gráfico
    FILE* gnuplotPipe = popen("gnuplot -persistent", "w");
    if (!gnuplotPipe) {
        std::cerr << "Erro ao abrir o pipe para o gnuplot!" << std::endl;
        return 1;
    }

    fprintf(gnuplotPipe, "set title 'Gráfico da função f(x) = |sin(x) + cos(x)|'\n");
    fprintf(gnuplotPipe, "set xlabel 'x'\n");
    fprintf(gnuplotPipe, "set ylabel 'f(x)'\n");
    fprintf(gnuplotPipe, "set grid\n");
    fprintf(gnuplotPipe, "plot 'function_data.dat' with lines title '|sin(x) + cos(x)|'\n");
    
    pclose(gnuplotPipe);

    return 0;
}