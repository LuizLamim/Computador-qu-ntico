#include <stdio.h>
#include <math.h>

int main() {
    double numero, resultado;

    printf("Digite um numero para elevar a 10a potencia: ");
    scanf("%lf", &numero);

    resultado = pow(numero, 10);

    printf("O numero %.2lf elevado a 10 e: %.2lf\n", numero, resultado);

    return 0;
}