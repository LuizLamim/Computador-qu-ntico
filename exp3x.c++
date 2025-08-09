#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

// A função que queremos plotar
double f(double x) {
    return exp(x) + 3 * x;
}

int main() {
    std::ofstream file("dados.dat");

    // Verifica se o arquivo foi aberto com sucesso
    if (!file.is_open()) {
        std::cerr << "Erro ao abrir o arquivo 'dados.dat'!" << std::endl;
        return 1;
    }

    double start = -5.0; // Início do intervalo
    double end = 5.0;    // Fim do intervalo
    double step = 0.1;   // Passo para cada ponto

    // Calcula os valores e escreve no arquivo
    for (double x = start; x <= end; x += step) {
        file << x << " " << f(x) << std::endl;
    }

    // O arquivo é fechado automaticamente quando 'file' sai do escopo
    // (destruído no final da função main)

    std::cout << "Dados da função salvos em 'dados.dat'." << std::endl;

    return 0;
}