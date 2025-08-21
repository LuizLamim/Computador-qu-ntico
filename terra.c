#include <stdio.h>
#include <math.h>

// Define a constante para o raio médio da Terra em quilômetros.
#define RAIO_TERRA_KM 6371.0

// Protótipo da função.
double calcular_curvatura(double distancia_km);

int main() {
    double distancia_km;
    double curvatura_metros;

    printf("--- Calculadora de Curvatura da Terra ---\n");
    printf("Este programa calcula a queda vertical (curvatura) da Terra \n");
    printf("para uma determinada distancia.\n");
    printf("------------------------------------------\n");

    printf("Digite a distancia em quilometros: ");

    // A função scanf retorna o número de itens lidos com sucesso.
    // Usar essa verificação evita comportamentos inesperados em caso de entrada inválida.
    if (scanf("%lf", &distancia_km) != 1 || distancia_km < 0) {
        printf("Entrada invalida. Por favor, digite um numero positivo.\n");
        return 1; // Retorna um código de erro.
    }

    curvatura_metros = calcular_curvatura(distancia_km);

    printf("\nPara uma distancia de %.2lf km, a curvatura (queda vertical) e de:\n", distancia_km);
    printf("%.2f metros.\n", curvatura_metros);
    printf("\n*Este calculo e uma aproximacao e desconsidera fatores como refracao atmosferica.\n");

    return 0; // Indica que o programa terminou com sucesso.
}

/**
 * @brief Calcula a curvatura da Terra (queda vertical) para uma determinada distancia.
 * @param distancia_km A distancia em quilometros.
 * @return A queda vertical em metros.
 */
double calcular_curvatura(double distancia_km) {
    // Calcula a queda vertical em quilômetros.
    double queda_vertical_km = (distancia_km * distancia_km) / (2 * RAIO_TERRA_KM);

    // Converte a queda vertical para metros.
    double queda_vertical_metros = queda_vertical_km * 1000;

    return queda_vertical_metros;
}