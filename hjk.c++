#include <iostream>

int main() {
    // Os três primeiros números primos são: 2, 3 e 5.

    int primeiro_primo = 2;
    int segundo_primo = 3;
    int terceiro_primo = 5;

    // Calcula a soma
    int soma = primeiro_primo + segundo_primo + terceiro_primo;

    std::cout << "Os 3 primeiros números primos são: "
              << primeiro_primo << ", "
              << segundo_primo << " e "
              << terceiro_primo << std::endl;

std::cout << "A soma dos 3 primeiros números primos é: "
              << soma << std::endl;

    return 0;
}