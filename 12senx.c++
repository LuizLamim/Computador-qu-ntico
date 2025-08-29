#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

// Define a função f(x)
double f(double x) {
    return 13 * cos(x);
}

int main() {
    // Cria um objeto para escrever no arquivo
    std::ofstream arquivo("dados.txt");

    // Verifica se o arquivo foi aberto com sucesso
    if (!arquivo.is_open()) {
        std::cerr << "Erro ao abrir o arquivo para escrita!" << std::endl;
        return 1;
    }

    // Define o intervalo e o número de pontos
    double inicio_x = -2 * M_PI;
    double fim_x = 2 * M_PI;
    int num_pontos = 1000;

    // Calcula o passo entre os pontos
    double passo = (fim_x - inicio_x) / (num_pontos - 1);

    // Loop para calcular e salvar os valores no arquivo
    for (int i = 0; i < num_pontos; ++i) {
        double x = inicio_x + i * passo;
        double y = f(x);
        arquivo << x << " " << y << std::endl;
    }

    // Fecha o arquivo
    arquivo.close();

    std::cout << "Dados da funcao salvos em 'dados.txt'." << std::endl;

    return 0;
}