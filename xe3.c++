#include <iostream>
#include <vector>
#include "gnuplot-iostream.h" // Inclui a biblioteca para Gnuplot

int main() {
    // Cria uma instância do Gnuplot
    Gnuplot gp;

    // Define o intervalo de x para o plot
    double x_min = -10.0;
    double x_max = 10.0;
    int num_points = 1000;

    // Cria os vetores para armazenar os dados de x e y
    std::vector<double> x_data;
    std::vector<double> y_data;

    // Loop para gerar os dados da função y = x^3
    for (int i = 0; i < num_points; ++i) {
        double x = x_min + (x_max - x_min) * i / (num_points - 1);
        double y = x * x * x; // Calcula x^3
        x_data.push_back(x);
        y_data.push_back(y);
    }

    // Configura o gráfico
    gp << "set title 'Gráfico da função f(x) = x^3'\n";
    gp << "set xlabel 'Eixo x'\n";
    gp << "set ylabel 'Eixo y'\n";
    gp << "set grid\n";

    // Plota o gráfico usando os dados que acabamos de gerar
    gp << "plot '-' with lines title 'f(x) = x^3' lc rgb 'blue'\n";
    gp.send1d(boost::make_tuple(x_data, y_data));

    // Exibe o gráfico até que uma tecla seja pressionada
    std::cout << "Pressione Enter para fechar o gráfico." << std::endl;
    std::cin.get();

    return 0;
}