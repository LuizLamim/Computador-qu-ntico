#include <iostream>
#include <fstream>
#include <cmath>

int main() {
    // 1. Cria e escreve os dados no arquivo 'data.dat'
    std::ofstream dataFile("data.dat");
    if (!dataFile.is_open()) {
        std::cerr << "Erro: não foi possível abrir o arquivo de dados." << std::endl;
        return 1;
    }

    const int numPoints = 100;
    const double range = 10.0;
    const double step = 2 * range / numPoints;

    for (int i = 0; i <= numPoints; ++i) {
        double x = -range + i * step;
        double y = x * x; // f(x) = x^2
        dataFile << x << " " << y << std::endl;
    }