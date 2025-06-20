#include <iostream>
#include <fstream>
#include <cmath> // Para a função pow()
#include <iomanip> // Para setprecision

int main() {
    double a, b;

    std::cout << "Digite o coeficiente 'a' da funcao exponencial (y = a * b^x): ";
    std::cin >> a;
    std::cout << "Digite a base 'b': ";
    std::cin >> b;

    // Abre um arquivo para escrita
    std::ofstream outputFile("dados_exp.txt");

    if (!outputFile.is_open()) {
        std::cerr << "Erro ao abrir o arquivo dados_exp.txt" << std::endl;
        return 1;
    }

    // Define a precisão para a saída dos números no arquivo
    outputFile << std::fixed << std::setprecision(6);

    // Gera os pontos para a plotagem
    // Você pode ajustar o intervalo (x_min, x_max) e o passo (step)
    double x_min = -5.0;
    double x_max = 5.0;
    double step = 0.1;

    for (double x = x_min; x <= x_max; x += step) {
        double y = a * std::pow(b, x); // Calcula a^b^x
        outputFile << x << " " << y << std::endl;
    }

    outputFile.close();
    std::cout << "Dados gerados com sucesso em 'dados_exp.txt'" << std::endl;

    // Exibe a equação para o usuário
    std::cout << "Funcao: " << a << " * " << b << "^x" << std::endl;
    std::cout << "Agora, use o Gnuplot para plotar os dados." << std::endl;
    std::cout << "Exemplo de comando Gnuplot: plot 'dados_exp.txt' with lines title '" << a << "*" << b << "^x'" << std::endl;

    return 0;
}