#include <iostream> // Inclui a biblioteca iostream para entrada e saída

int main() { // Função principal onde a execução do programa começa
    // Declaração de variáveis para armazenar os números e o resultado
    int numero1;
    int numero2;
    int soma;

    // Solicita ao usuário para digitar o primeiro número
    std::cout << "Digite o primeiro número: ";
    std::cin >> numero1; // Lê o primeiro número digitado pelo usuário

    // Solicita ao usuário para digitar o segundo número
    std::cout << "Digite o segundo número: ";
    std::cin >> numero2; // Lê o segundo número digitado pelo usuário

    // Realiza a soma dos dois números
    soma = numero1 + numero2;

    // Exibe o resultado da soma
    std::cout << "A soma é: " << soma << std::endl;

    return 0; // Retorna 0 para indicar que o programa foi executado com sucesso
}