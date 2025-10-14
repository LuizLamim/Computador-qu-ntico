#include <iostream>

// Função para elevar um número ao quadrado usando a multiplicação
double quadrado_multiplicacao(double numero) {
    return numero * numero;
}

int main() {
    double num;
    
    std::cout << "Digite um número: ";
    
    if (!(std::cin >> num)) {
        std::cerr << "Entrada inválida. Por favor, digite um número.\n";
        return 1;
    }
    
    double resultado = quadrado_multiplicacao(num);
    
    std::cout << "O quadrado de " << num << " é: " << resultado << std::endl;
    
    return 0;
}
    