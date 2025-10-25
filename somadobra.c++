#include <iostream>

// Função principal onde o programa começa a execução
int main() {
    // Declaração de variáveis para armazenar os dois números de entrada
    double numero1;
    double numero2;

    // Variável para armazenar o resultado da soma
    double soma;

    // Variável para armazenar o resultado final (soma dobrada)
    double resultado_dobrado;

    // 1. Pede a entrada do primeiro número
    std::cout << "Por favor, insira o primeiro número: ";
    // Lê o primeiro número digitado pelo usuário
    std::cin >> numero1;

    // 2. Pede a entrada do segundo número
    std::cout << "Por favor, insira o segundo número: ";
    // Lê o segundo número digitado pelo usuário
    std::cin >> numero2;

    // 3. Calcula a soma dos dois números
    soma = numero1 + numero2;

    // 4. Dobra o valor da soma
    resultado_dobrado = soma * 2;

    // Exibe os resultados intermediários e o final
    std::cout << "\n--- Resultados ---" << std::endl;
    std::cout << "O primeiro número inserido foi: " << numero1 << std::endl;
    std::cout << "O segundo número inserido foi: " << numero2 << std::endl;
    std::cout << "A soma dos dois números é: " << soma << std::endl;
    std::cout << "O resultado dobrado da soma é: " << resultado_dobrado << std::endl;

    // Indica que o programa terminou com sucesso
    return 0;
}