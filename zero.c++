#include <iostream>
#include <vector>

int main() {
    // Cria uma matriz 4x4 de zeros usando std::vector
    std::vector<std::vector<int>> matriz(4, std::vector<int>(4, 0));

    std::cout << "Matriz 4x4 de Zeros:" << std::endl;
    for (const auto& linha : matriz) {
        for (const auto& elemento : linha) {
            std::cout << elemento << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}