#include <iostream> // Necessário para usar cout

int main() {
    // Imprimir letras minúsculas
    std::cout << "Alfabeto minúsculo:\n";
    for (char letra = 'a'; letra <= 'z'; ++letra) {
        std::cout << letra << " ";
    }
    std::cout << "\n\n"; // Duas quebras de linha para espaçamento

    // Imprimir letras maiúsculas
    std::cout << "Alfabeto maiúsculo:\n";
    for (char letra = 'A'; letra <= 'Z'; ++letra) {
        std::cout << letra << " ";
    }
    std::cout << "\n"; // Quebra de linha final

    return 0; // Indica que o programa terminou com sucesso
}