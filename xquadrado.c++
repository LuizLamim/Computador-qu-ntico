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