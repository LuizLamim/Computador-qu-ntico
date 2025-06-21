#include <iostream>
#include <fstream>
#include <cmath>   // Para std::sin e M_PI
#include <iomanip> // Para std::setprecision
#include <string>  // Para std::string

// Define M_PI se não estiver definido (alguns compiladores C++ podem não ter)
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

int main() {
    // Nome do arquivo onde os dados serão salvos
    const std::string filename = "integral_cosseno_data.txt";
    std::ofstream outputFile(filename);

    if (!outputFile.is_open()) {
        std::cerr << "Erro ao abrir o arquivo para escrita: " << filename << std::endl;
        return 1;
    }

    // Intervalo de x para o gráfico (por exemplo, de -2*pi a 2*pi)
    double start_x = -2 * M_PI;
    double end_x = 2 * M_PI;
    int num_points = 1000; // Número de pontos para maior suavidade do gráfico

    double step_x = (end_x - start_x) / (num_points - 1);

    // Escreve os pontos (x, sin(x)) no arquivo
    for (int i = 0; i < num_points; ++i) {
        double x = start_x + i * step_x;
        double y = std::sin(x); // A integral do cosseno de x (ignorando a constante de integração)
        outputFile << std::fixed << std::setprecision(6) << x << " " << y << std::endl;
    }

    outputFile.close();
    std::cout << "Dados gerados e salvos em: " << filename << std::endl;

    // --- Parte para plotar com Gnuplot (necessário ter Gnuplot instalado) ---
    // Você pode chamar o Gnuplot diretamente do C++ ou executar o comando manualmente.

    // Exemplo de como gerar um comando Gnuplot e executá-lo via C++
    // Atenção: Isso só funcionará se o Gnuplot estiver no PATH do sistema.
    std::string gnuplot_command = "gnuplot -persistent -e \"set title 'Gráfico da Integral do Cosseno de X'; set xlabel 'X'; set ylabel 'Sen(X)'; plot '" + filename + "' with lines title 'Sen(X)'\"";
    
    // Usa system() para executar o comando.
    // Lembre-se que system() pode ser inseguro em algumas aplicações
    // e deve ser usado com cautela.
    int result = system(gnuplot_command.c_str());

    if (result == 0) {
        std::cout << "Gnuplot invocado com sucesso (se instalado)." << std::endl;
    } else {
        std::cerr << "Falha ao invocar Gnuplot. Certifique-se de que está instalado e no PATH." << std::endl;
        std::cerr << "Comando tentado: " << gnuplot_command << std::endl;
    }

    return 0;
}