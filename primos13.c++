#include <vector>
#include <cmath>
#include <iomanip>

bool ehPrimo(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i <= std::sqrt(n); ++i) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    std::vector<int> primos;
    int numeroAtual = 2;
    const int NUM_PRIMOS = 13;

    std::cout << "Os primeiros " << NUM_PRIMOS << " números primos são:\n";
    std::cout << "------------------------------------------\n";

    while (primos.size() < NUM_PRIMOS) {
        if (ehPrimo(numeroAtual)) {
            primos.push_back(numeroAtual);
        }
        numeroAtual++;
    }

    std::cout << std::setw(8) << "Índice" << " | " << std::setw(8) << "Valor Primo" << "\n";
    std::cout << "------------------------------------------\n";

    for (size_t i = 0; i < primos.size(); ++i) {
        std::cout << std::setw(8) << (i + 1)
                  << " | "
                  << std::setw(8) << primos[i]
                  << "\n";
    }