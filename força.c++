#include <iostream>
#include <fstream>
#include <iomanip>

int main() {
    // Definir a massa (m) como uma constante
    const double massa = 10.0; // em kg
    
    // Abrir o arquivo para escrita
    std::ofstream arquivo("dados_F_vs_a.txt");

    // Verificar se o arquivo foi aberto corretamente
    if (!arquivo.is_open()) {
        std::cerr << "Erro ao abrir o arquivo!" << std::endl;
        return 1;
    }
    
    // Escrever o cabeçalho no arquivo
    arquivo << "Aceleracao\tForca\n";
    
    // Gerar os dados para aceleração de 0 a 10
    for (int i = 0; i <= 100; ++i) {
        double aceleracao = static_cast<double>(i) / 10.0; // de 0.0 a 10.0
        double forca = massa * aceleracao;   // F = m * a
        
        // Escrever os dados no arquivo com precisão de duas casas decimais
        arquivo << std::fixed << std::setprecision(2)
                << aceleracao << "\t\t" << forca << "\n";
    }
    
    // O arquivo é fechado automaticamente quando 'arquivo' sai de escopo
    
    std::cout << "Dados gerados com sucesso no arquivo 'dados_F_vs_a.txt'." << std::endl;
    std::cout << "Você pode usar um software como Gnuplot ou Excel para plotar o gráfico." << std::endl;
    
    return 0;
}