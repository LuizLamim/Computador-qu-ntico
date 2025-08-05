#include <iostream>
#include <iomanip> // Necessário para usar std::fixed e std::setprecision

// Função para calcular a aceleração
float calcularAceleracao(float velocidadeInicial, float velocidadeFinal, float tempo) {
    // A fórmula da aceleração é: a = (velocidade_final - velocidade_inicial) / tempo
    return (velocidadeFinal - velocidadeInicial) / tempo;
}

int main() {
    // Declaração das variáveis
    float velocidadeInicial;
    float velocidadeFinal;
    float tempo;

    std::cout << "--- Calculadora de Aceleracao ---" << std::endl;
    std::cout << "A aceleracao e a taxa de variacao de velocidade ao longo do tempo." << std::endl;

    // Solicita a entrada do usuário
    std::cout << "Digite a velocidade inicial (em m/s): ";
    std::cin >> velocidadeInicial;

    std::cout << "Digite a velocidade final (em m/s): ";
    std::cin >> velocidadeFinal;

    std::cout << "Digite o tempo decorrido (em segundos): ";
    std::cin >> tempo;

    // Verifica se o tempo e zero para evitar a divisao por zero
    if (tempo == 0) {
        std::cerr << "Erro: O tempo decorrido nao pode ser zero." << std::endl;
        return 1; // Retorna 1 para indicar um erro
    }

    // Chama a funcao para calcular a aceleracao
    float aceleracao = calcularAceleracao(velocidadeInicial, velocidadeFinal, tempo);

    // Exibe o resultado com formatação
    std::cout << "\nResultados:" << std::endl;
    std::cout << std::fixed << std::setprecision(2); // Formata para 2 casas decimais
    std::cout << "Velocidade Inicial: " << velocidadeInicial << " m/s" << std::endl;
    std::cout << "Velocidade Final: " << velocidadeFinal << " m/s" << std::endl;
    std::cout << "Tempo Decorrido: " << tempo << " s" << std::endl;
    std::cout << "A Aceleracao e: " << aceleracao << " m/s²" << std::endl;
    std::cout << "----------------------------------" << std::endl;

    return 0; // Retorna 0 para indicar que o programa foi executado com sucesso
}