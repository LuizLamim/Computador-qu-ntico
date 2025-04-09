#include <stdio.h>
#include <math.h>

int main() {
  // Declaração das variáveis
  double capitalInicial, taxaJuros, montanteFinal;
  int periodo;

  // Solicita ao usuário que insira os dados
  printf("Digite o capital inicial (em R$): ");
  scanf("%lf", &capitalInicial);

  printf("Digite a taxa de juros mensal (em %%): ");
  scanf("%lf", &taxaJuros);

  printf("Digite o período em meses: ");
  scanf("%d", &periodo);

  // Converte a taxa de juros para decimal
  taxaJuros = taxaJuros / 100.0;

  // Calcula o montante final usando a fórmula de juros compostos
  montanteFinal = capitalInicial * pow(1 + taxaJuros, periodo);

  // Exibe o resultado
  printf("\n--- Resultado ---\n");
  printf("Capital Inicial: R$ %.2f\n", capitalInicial);
  printf("Taxa de Juros Mensal: %.2f%%\n", taxaJuros * 100);
  printf("Período (meses): %d\n", periodo);
  printf("Montante Final: R$ %.2f\n", montanteFinal);

  return 0;
}