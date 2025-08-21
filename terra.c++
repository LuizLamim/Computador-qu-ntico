#include <iostream>
#include <cmath>
#include <limits>

// Define a constante para o raio médio da Terra em quilômetros.
const double RAIO_TERRA_KM = 6371.0;

// Protótipo da função.
double calcular_curvatura(double distancia_km);

int main() {
    double distancia_km;

    std::cout << "--- Calculadora de Curvatura da Terra ---" << std::endl;
    std::cout << "Este programa calcula a queda vertical (curvatura) da Terra " << std::endl;
    std::cout << "para uma determinada distancia." << std::endl;
    std::cout << "------------------------------------------" << std::endl;

    std::cout << "Digite a distancia em quilometros: ";
    std::cin >> distancia_km;

    // Verifica se a entrada eh valida.
    // std::cin.fail() checa se o ultimo 'cin' falhou.
    if (std::cin.fail() || distancia_km < 0) {
        std::cout << "Entrada invalida. Por favor, digite um numero positivo." << std::endl;
        return 1;
    }

    double curvatura_metros = calcular_curvatura(distancia_km);

    // Formata a saida com duas casas decimais.
    std::cout.precision(2);
    std::cout << std::fixed;

    std::cout << "\nPara uma distancia de " << distancia_km << " km, a curvatura (queda vertical) e de:" << std::endl;
    std::cout << curvatura_metros << " metros." << std::endl;
    std::cout << "\n*Este calculo e uma aproximacao e desconsidera fatores como refracao atmosferica." << std::endl;

    return 0;
}

/**
 * @brief Calcula a curvatura da Terra (queda vertical) para uma determinada distancia.
 * @param distancia_km A distancia em quilometros.
 * @return A queda vertical em metros.
 */
double calcular_curvatura(double distancia_km) {
    // Calcula a queda vertical em quilômetros.
    // A funcao pow(base, expoente) pode ser usada para potencia.
    double queda_vertical_km = std::pow(distancia_km, 2) / (2 * RAIO_TERRA_KM);

    // Converte a queda vertical para metros.
    double queda_vertical_metros = queda_vertical_km * 1000;

    return queda_vertical_metros;
}