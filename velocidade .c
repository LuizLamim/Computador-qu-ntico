#include <stdio.h>

// Função para calcular a aceleração
float calcular_aceleracao(float velocidade_inicial, float velocidade_final, float tempo) {
    // A fórmula da aceleração é: a = (velocidade_final - velocidade_inicial) / tempo
    return (velocidade_final - velocidade_inicial) / tempo;
}

int main() {
    // Declaração das variáveis
    float velocidade_inicial;
    float velocidade_final;
    float tempo;
    float aceleracao;

    printf("--- Calculadora de Aceleracao ---\n");
    printf("A aceleracao e a taxa de variacao de velocidade ao longo do tempo.\n");

    // Solicita a entrada do usuário
    printf("Digite a velocidade inicial (em m/s): ");
    scanf("%f", &velocidade_inicial);

    printf("Digite a velocidade final (em m/s): ");
    scanf("%f", &velocidade_final);

    printf("Digite o tempo decorrido (em segundos): ");
    scanf("%f", &tempo);

    // Verifica se o tempo e zero para evitar a divisao por zero
    if (tempo == 0) {
        printf("Erro: O tempo decorrido nao pode ser zero.\n");
        return 1; // Retorna 1 para indicar um erro
    }

    // Chama a funcao para calcular a aceleracao
    aceleracao = calcular_aceleracao(velocidade_inicial, velocidade_final, tempo);

    // Exibe o resultado
    printf("\nResultados:\n");
    printf("Velocidade Inicial: %.2f m/s\n", velocidade_inicial);
    printf("Velocidade Final: %.2f m/s\n", velocidade_final);
    printf("Tempo Decorrido: %.2f s\n", tempo);
    printf("A Aceleracao e: %.2f m/s²\n", aceleracao);
    printf("----------------------------------\n");

    return 0; // Retorna 0 para indicar que o programa foi executado com sucesso
}