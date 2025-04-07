#include <stdio.h>
#include <math.h> // Para usar a função pow para calcular o quadrado da altura

int main() {
  float peso, altura, imc;

  // Solicita ao usuário que digite o peso
  printf("Digite o seu peso em quilogramas (kg): ");
  scanf("%f", &peso);

  // Solicita ao usuário que digite a altura
  printf("Digite a sua altura em metros (m): ");
  scanf("%f", &altura);

  // Verifica se a altura é válida (maior que zero) para evitar divisão por zero
  if (altura <= 0) {
    printf("Altura inválida. Por favor, digite um valor maior que zero.\n");
    return 1; // Indica que ocorreu um erro
  }

  // Calcula o Índice de Massa Corporal (IMC)
  imc = peso / pow(altura, 2);

  // Exibe o resultado do IMC
  printf("Seu IMC é: %.2f\n", imc);

  // Classifica o IMC de acordo com as faixas comuns
  printf("Classificação do IMC:\n");
  if (imc < 18.5) {
    printf("Abaixo do peso\n");
  } else if (imc < 25) {
    printf("Peso normal\n");
  } else if (imc < 30) {
    printf("Sobrepeso\n");
  } else if (imc < 35) {
    printf("Obesidade grau I\n");
  } else if (imc < 40) {
    printf("Obesidade grau II\n");
  } else {
    printf("Obesidade grau III (mórbida)\n");
  }

  return 0; // Indica que o programa foi executado com sucesso
}