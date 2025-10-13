#include <iostream>

// Função principal onde a execução do programa começa
int main() {
    // Declaração de variáveis para armazenar os dois números e o resultado
    double numero1;
    double numero2;
    double resultado;

    // Solicita ao usuário para inserir o primeiro número
    std::cout << "Digite o primeiro número: ";
    // Lê o primeiro número inserido pelo usuário e armazena em 'numero1'
    std::cin >> numero1;

    // Solicita ao usuário para inserir o segundo número
    std::cout << "Digite o segundo número: ";
    // Lê o segundo número inserido pelo usuário e armazena em 'numero2'
    std::cin >> numero2;

    // Realiza a multiplicação
    resultado = numero1 * numero2;

    // Exibe o resultado da multiplicação
    std::cout << "O produto de " << numero1 << " e " << numero2 << " é: " << resultado << std::endl;

    // Retorna 0 para indicar que o programa foi executado com sucesso