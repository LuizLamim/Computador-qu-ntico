#include <iostream> // Inclui a biblioteca iostream para entrada e saída

int main() { // Função principal onde a execução do programa começa
    // Declaração de variáveis para armazenar os números e o resultado
    int numero1;
    int numero2;
    int subtracao; // Alteramos o nome da variável para 'subtracao'

    // Solicita ao usuário para digitar o primeiro número (minuendo)
    std::cout << "Digite o primeiro número (minuendo): ";
    std::cin >> numero1; // Lê o primeiro número digitado pelo usuário

    // Solicita ao usuário para digitar o segundo número (subtraendo)
    std::cout << "Digite o segundo número (subtraendo): ";
    std::cin >> numero2; // Lê o segundo número digitado pelo usuário

    // Realiza a subtração dos dois números
    subtracao = numero1 - numero2; // A operação agora é de subtração

    // Exibe o resultado da subtração
    std::cout << "A subtração é: " << subtracao << std::endl;

    return 0; // Retorna 0 para indicar que o programa foi executado com sucesso
}