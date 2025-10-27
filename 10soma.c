#include <stdio.h>

int main() {
    int n = 10;          
    int soma = 0;        
    int i;               

    for (i = 1; i <= n; i++) {
        soma = soma + i; 
    }

    printf("A soma dos primeiros %d numeros inteiros positivos e: %d\n", n, soma);

    return 0;
}