#include <vector>
#include <cmath>
#include <string>
#include "matplotlibcpp.h"

namespace plt = matplotlibcpp;

int main() {
    // Vetores para armazenar os dados de x e y
    std::vector<double> x, y;

    // Gerar os pontos
    for (double i = 0.01; i <= 10.0; i += 0.01) {
        x.push_back(i);
        y.push_back(std::fabs(std::log(i)));
    }

    // Configurar o gráfico
    plt::title("Gráfico da função f(x) = |log(x)|");
    plt::xlabel("Eixo x");
    plt::ylabel("Eixo y");
    plt::grid(true);

    // Plotar a linha
    plt::plot(x, y, {{"label", "f(x) = |log(x)|"}});

    // Adicionar legenda e exibir o gráfico
    plt::legend();
    plt::show();

    return 0;
}