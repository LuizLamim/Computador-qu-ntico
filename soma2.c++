#include <iostream>


int main() {
    double numero1, numero2, soma;

    std::cout << "Por favor, insira o primeiro número: ";

    std::cin >> numero1;

    std::cout << "Por favor, insira o segundo número: ";

    std::cin >> numero2;

    soma = numero1 + numero2;

    std::cout << "A soma de " << numero1 << " e " << numero2 << " é: " << soma << std::endl;

    return 0;
}
