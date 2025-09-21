#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

// Função para calcular o valor de f(x)
double f(double x) {
    return 3 * pow(x, 2) + 3 * x;
}

int main() {
    // Nome do arquivo de dados que será gerado
    const std::string data_filename = "dados.dat";

    // Intervalo de x
    const double x_min = -10.0;
    const double x_max = 10.0;
    const double step = 0.1; // "Resolução" do gráfico

    // Abre o arquivo para escrita
    std::ofstream data_file(data_filename);

    if (!data_file.is_open()) {
        std::cerr << "Erro ao criar o arquivo de dados." << std::endl;
        return 1;
    }