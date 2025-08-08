#include <iostream>
#include <fstream>
#include <cmath>

#define PI 3.14159265358979323846
#define NUM_PONTOS 400

int main() {
    // Abre o arquivo para escrita
    std::ofstream arquivo("dados.txt");

    // Verifica se o arquivo foi aberto com sucesso
    if (!arquivo.is_open()) {
        std::cerr << "Erro ao abrir o arquivo dados.txt" << std::endl;
        return 1;
    }

    double x, y_funcao, y_constante;
    double passo = (4 * PI) / (NUM_PONTOS - 1);

    // Escreve os cabeçalhos das colunas no arquivo
    arquivo << "# x  y_funcao  y_constante" << std::endl;

    // Loop para calcular os valores da função e da constante
    for (int i = 0; i < NUM_PONTOS; i++) {
        x = -2 * PI + i * passo;
        y_funcao = 3 * sin(x) + 25 * cos(x);
        y_constante = 18.0;

        // Salva os valores no arquivo
        arquivo << x << " " << y_funcao << " " << y_constante << std::endl;
    }

    // Fecha o arquivo
    arquivo.close();

    std::cout << "Dados gerados com sucesso para o arquivo dados.txt" << std::endl;

    return 0;
}