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

    // Escreve os dados no arquivo
    for (double x = x_min; x <= x_max; x += step) {
        double y = f(x);
        data_file << x << " " << y << std::endl;
    }

    // Fecha o arquivo
    data_file.close();

    // Comando Gnuplot para plotar os dados
    std::string gnuplot_command =
        "gnuplot -e \"set title 'Gráfico de 3x^2 + 3x'; "
        "set xlabel 'Eixo X'; "
        "set ylabel 'Eixo Y'; "
        "plot '" + data_filename + "' with lines title '3x^2 + 3x'\"";

    // Executa o comando Gnuplot
    std::cout << "Gerando gráfico com Gnuplot..." << std::endl;
    int result = system(gnuplot_command.c_str());

    if (result != 0) {
        std::cerr << "Erro ao executar o comando Gnuplot. Verifique se o Gnuplot está instalado e no seu PATH." << std::endl;
        return 1;
    }

    std::cout << "Gráfico gerado com sucesso!" << std::endl;

    return 0;
}