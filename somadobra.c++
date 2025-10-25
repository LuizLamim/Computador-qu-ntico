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