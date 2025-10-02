#include <stdio.h>
#include <stdbool.h>

// Função para verificar se um número é primo
bool eh_primo(int num) {
    if (num <= 1) {
        return false;
    }
    // Testamos divisibilidade até a raiz quadrada de 'num' para otimizar
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

