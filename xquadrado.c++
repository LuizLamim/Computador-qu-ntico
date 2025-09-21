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

    dataFile.close();
    std::cout << "Arquivo de dados 'data.dat' criado com sucesso." << std::endl;

    // 2. Cria o script para o Gnuplot
    std::ofstream scriptFile("plot.gp");
    if (!scriptFile.is_open()) {
        std::cerr << "Erro: não foi possível criar o script Gnuplot." << std::endl;
        return 1;
    }
    
    scriptFile << "set title 'Gráfico de y = x^2'" << std::endl;
    scriptFile << "set xlabel 'Eixo X'" << std::endl;
    scriptFile << "set ylabel 'Eixo Y'" << std::endl;
    scriptFile << "set grid" << std::endl;
    scriptFile << "plot 'data.dat' with lines title 'y = x^2'" << std::endl;
    scriptFile.close();
    std::cout << "Script Gnuplot 'plot.gp' criado com sucesso." << std::endl;

    // 3. Executa o Gnuplot a partir do programa
    // Este comando só funciona se o gnuplot estiver no seu PATH
    int result = system("gnuplot -persistent plot.gp");
    if (result != 0) {
        std::cerr << "Erro: falha ao executar o Gnuplot. Certifique-se de que ele está instalado e no seu PATH." << std::endl;
        return 1;
    }

    return 0;
}

