#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>

int main() {
    // Cria um objeto para o arquivo de saída
    std::ofstream arquivo("dados.dat");

    // Verifica se o arquivo foi aberto com sucesso
    if (!arquivo.is_open()) {
        std::cerr << "Erro ao abrir o arquivo 'dados.dat'." << std::endl;
        return 1;
    }

    int num_pontos = 80;
    double inicio = 0.1;
    double fim = 10.0;
    double passo = (fim - inicio) / (num_pontos - 1);

    // Itera para calcular e salvar os dados
    for (int i = 0; i < num_pontos; ++i) {
        double x = inicio + i * passo;
        double y = std::log10(x) + 10.0;
        
        // Salva os valores de x e y no arquivo
        arquivo << std::fixed << std::setprecision(6) << x << " " << y << std::endl;
    }

    // Fecha o arquivo
    arquivo.close();

    std::cout << "Dados da função salvos em 'dados.dat'." << std::endl;

    return 0;
}