#include <stdio.h>
#include <math.h>

int main() {
  float raio, volume;
  const float PI = 3.14159; // Define a constante PI

  // Solicita ao usuário que digite o raio da esfera
  printf("Digite o raio da esfera: ");
  scanf("%f", &raio);

  // Calcula o volume da esfera usando a fórmula: V = (4/3) * PI * r^3
  volume = (4.0/3.0) * PI * pow(raio, 3);

  // Exibe o resultado
  printf("O volume da esfera com raio %.2f eh: %.2f\n", raio, volume);

  return 0;
}