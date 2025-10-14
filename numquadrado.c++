#include <iostream>

// Função para elevar um número ao quadrado usando a multiplicação
double quadrado_multiplicacao(double numero) {
    return numero * numero;
}

int main() {
    double num;

    std::cout << "Digite um número: ";
    
    // Armazena a entrada do usuário na variável 'num'
    if (!(std::cin >> num)) {
        std::cerr << "Entrada inválida. Por favor, digite um número.\n";
        return 1;
    }
    
    // Calcula o quadrado
    double resultado = quadrado_multiplicacao(num);
    