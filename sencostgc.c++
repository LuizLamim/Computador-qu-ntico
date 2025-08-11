#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

const double PI = 3.14159265358979323846;

// Função para criar os arquivos de dados para o Gnuplot
void create_data_files() {
    std::ofstream seno_file("seno.dat");
    std::ofstream cosseno_file("cosseno.dat");
    std::ofstream tangente_file("tangente.dat");

    if (!seno_file.is_open() || !cosseno_file.is_open() || !tangente_file.is_open()) {
        std::cerr << "Erro ao abrir os arquivos de dados." << std::endl;
        exit(1);
    }

    // Gerar os dados no intervalo de -2*PI a 2*PI
    for (double x = -2 * PI; x <= 2 * PI; x += 0.05) {
        seno_file << x << " " << std::sin(x) << std::endl;
        cosseno_file << x << " " << std::cos(x) << std::endl;

        // Verifica o cosseno para evitar assíntotas na tangente
        if (std::abs(std::cos(x)) > 1e-6) {
            tangente_file << x << " " << std::tan(x) << std::endl;
        }
    }

    seno_file.close();
    cosseno_file.close();
    tangente_file.close();
    
    std::cout << "Arquivos de dados criados com sucesso." << std::endl;
}

// Função para criar o script do Gnuplot
void create_gnuplot_script() {
    std::ofstream gnuplot_script("plot_functions.gp");

    if (!gnuplot_script.is_open()) {
        std::cerr << "Erro ao abrir o arquivo do script do Gnuplot." << std::endl;
        exit(1);
    }

    // Escrever os comandos para o Gnuplot
    gnuplot_script << "set terminal pngcairo enhanced font 'arial,12'\n";
    gnuplot_script << "set output 'functions.png'\n";
    gnuplot_script << "set title 'Funcoes Trigonometricas'\n";
    gnuplot_script << "set xlabel 'x'\n";
    gnuplot_script << "set ylabel 'y'\n";
    gnuplot_script << "set grid\n";
    gnuplot_script << "set xrange [-7:7]\n";
    gnuplot_script << "set yrange [-5:5]\n";
    gnuplot_script << "set key top left\n";
    gnuplot_script << "plot 'seno.dat' with lines title 'sin(x)', \\\n";
    gnuplot_script << "'cosseno.dat' with lines title 'cos(x)', \\\n";
    gnuplot_script << "'tangente.dat' with lines title 'tan(x)'\n";

    gnuplot_script.close();

    std::cout << "Script do Gnuplot criado com sucesso." << std::endl;
}

int main() {
    // 1. Cria os arquivos com os dados
    create_data_files();

    // 2. Cria o script para o gnuplot
    create_gnuplot_script();

    // 3. Executa o gnuplot
    std::cout << "Executando o Gnuplot..." << std::endl;
    // O comando "gnuplot" executa a ferramenta e o nome do arquivo
    // do script informa quais comandos ele deve seguir.
    system("gnuplot plot_functions.gp");

    std::cout << "Plotagem concluída. O gráfico foi salvo em 'functions.png'." << std::endl;

    return 0;
}