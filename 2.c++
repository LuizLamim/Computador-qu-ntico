#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip> // Para setprecision

int main() {
    double a, b, c;

    std::cout << "Digite o coeficiente 'a' da equacao (ax^2 + bx + c): ";
    std::cin >> a;
    std::cout << "Digite o coeficiente 'b': ";
    std::cin >> b;
    std::cout << "Digite o coeficiente 'c': ";
    std::cin >> c;

    // Abre um arquivo para escrita
    std::ofstream outputFile("dados.txt");

    if (!outputFile.is_open()) {
        std::cerr << "Erro ao abrir o arquivo dados.txt" << std::endl;
        return 1;
    }

    // Define a precisão para a saída dos números no arquivo
    outputFile << std::fixed << std::setprecision(6);

    // Gera os pontos para a plotagem
    // Você pode ajustar o intervalo (x_min, x_max) e o passo (step)
    double x_min = -10.0;
    double x_max = 10.0;
    double step = 0.1;

    for (double x = x_min; x <= x_max; x += step) {
        double y = a * x * x + b * x + c;
        outputFile << x << " " << y << std::endl;
    }

    outputFile.close();
    std::cout << "Dados gerados com sucesso em 'dados.txt'" << std::endl;

    // Exibe a equação para o usuário
    std::cout << "Equacao: " << a << "x^2 + " << b << "x + " << c << std::endl;
    std::cout << "Agora, use o Gnuplot para plotar os dados." << std::endl;
    std::cout << "Exemplo de comando Gnuplot: plot 'dados.txt' with lines title '" << a << "x^2 + " << b << "x + " << c << "'" << std::endl;


    return 0;
}