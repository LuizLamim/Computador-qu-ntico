#include <stdio.h>

int main() {
    int count = 0; // Contador de números primos encontrados
    int num = 2;   // Número a ser verificado, começa em 2
    
    printf("Os 5 primeiros numeros primos sao:\n");

    while (count < 5) {
        int isPrime = 1; // Flag para verificar se o número é primo. 1 = true, 0 = false

        // Verificação de primalidade
        // Para otimizar, a verificação pode ir até a raiz quadrada de 'num'
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                isPrime = 0; // Se for divisível, não é primo
                break;       // Sai do loop, não precisa continuar a verificação
            }
        }

        // Se a flag isPrime for 1, o número é primo
        if (isPrime == 1) {
            printf("%d\n", num);
            count++; // Incrementa o contador de primos
        }

        num++; // Passa para o próximo número
    }