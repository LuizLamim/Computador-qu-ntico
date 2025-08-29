#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

// A macro para compatibilidade com popen/pclose em diferentes sistemas operacionais
#ifdef _WIN32
    #define popen _popen
    #define pclose _pclose
#endif

// Constantes
const int NUM_PONTOS = 1000;
const double PI = 3.14159265358979323846;

int main() {
    // Definindo os semi-eixos para uma elipse com alta excentricidade
    // Quando 'b' é muito menor que 'a', a excentricidade 'e' se aproxima de 1.
    const double a = 5.0; // Semi-eixo maior
    const double b = 1.0; // Semi-eixo menor

    // Calculando a excentricidade
    const double excentricidade = std::sqrt(1.0 - (b * b) / (a * a));

    // Abrindo um arquivo para salvar os pontos da elipse
    std::ofstream data_file("dados_elipse.txt");
    if (!data_file.is_open()) {
        std::cerr << "Erro ao abrir o arquivo para escrita." << std::endl;
        return 1;
    }

    // Gerando os pontos da elipse
    for (int i = 0; i <= NUM_PONTOS; i++) {
        double theta = static_cast<double>(i) / NUM_PONTOS * 2.0 * PI;
        double x = a * std::cos(theta);
        double y = b * std::sin(theta);
        data_file << x << " " << y << "\n";
    }

    // Fechando o arquivo
    data_file.close();

    std::cout << "Pontos da elipse salvos em dados_elipse.txt" << std::endl;
    std::cout << "Gerando o gráfico com Gnuplot..." << std::endl;

    // Abrindo um pipe para o Gnuplot
    FILE* gnuplotPipe = popen("gnuplot -persistent", "w");
    if (!gnuplotPipe) {
        std::cerr << "Erro ao abrir pipe para o Gnuplot." << std::endl;
        return 1;
    }

    // Criando a string de comandos para o Gnuplot
    std::string command = "set title 'Gráfico de uma Elipse com Excentricidade Alta (e = " + std::to_string(excentricidade) + ")'\n";
    command += "set xlabel 'Eixo X'\n";
    command += "set ylabel 'Eixo Y'\n";
    command += "set size ratio -1\n"; // Força a proporção 1:1
    command += "plot 'dados_elipse.txt' with lines notitle\n";

    // Enviando os comandos para o Gnuplot
    fprintf(gnuplotPipe, "%s", command.c_str());

    // Fechando o pipe
    pclose(gnuplotPipe);

    return 0;
}