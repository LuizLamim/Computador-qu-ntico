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

int main() {
    int contador = 0;
    int numero_atual = 2;
    
    printf("Os 3 primeiros números primos são:\n");

    // Loop para encontrar os 3 primeiros primos
    while (contador < 3) {
        if (eh_primo(numero_atual)) {
            printf("%d ", numero_atual);
            contador++;
        }
        // Incrementamos e passamos para o próximo número
        numero_atual++;
    }
    
    printf("\n");

    return 0;
}