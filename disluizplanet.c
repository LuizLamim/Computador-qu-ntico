#include <stdio.h> // Para entrada e saída (printf, scanf)
#include <stdlib.h> // Para a função atof (ASCII para float) e para o system("cls") ou system("clear")
#include <string.h> // Para funções de string como strchr e strlen

// Definindo a velocidade da luz em km/s
#define VELOCIDADE_LUZ_KM_POR_SEGUNDO 299792.458

int main() {
    char distancia_km_str[100]; // Buffer para armazenar a entrada da distância como string
    double distancia_km;        // Variável para armazenar a distância em ponto flutuante
    double tempo_segundos;
    double tempo_minutos;
    double tempo_horas;
    double tempo_dias;

    // Limpa a tela do console (funciona no Windows e Linux/macOS)
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif

    printf("--- Calculadora de Tempo de Viagem da Luz ---\n");

    while (1) {
        printf("Digite a distância entre a Terra e o planeta em quilômetros (ex: 150.000.000 para Marte): ");
        if (fgets(distancia_km_str, sizeof(distancia_km_str), stdin) == NULL) {
            printf("Erro ao ler a entrada. Tente novamente.\n");
            continue;
        }

        // Remove o caractere de nova linha '\n' que fgets pode incluir
        distancia_km_str[strcspn(distancia_km_str, "\n")] = 0;

        // Tenta remover pontos e substituir vírgulas por pontos para garantir a conversão correta
        // Isso é uma simplificação. Para uma validação robusta, seria necessário um parser mais complexo.
        for (int i = 0; i < strlen(distancia_km_str); i++) {
            if (distancia_km_str[i] == '.') {
                memmove(&distancia_km_str[i], &distancia_km_str[i + 1], strlen(distancia_km_str) - i);
                i--; // Decrementa i para reavaliar o mesmo índice caso haja outro ponto
            } else if (distancia_km_str[i] == ',') {
                distancia_km_str[i] = '.';
            }
        }
        
        // Converte a string para um número de ponto flutuante
        distancia_km = atof(distancia_km_str);

        if (distancia_km < 0) {
            printf("A distância não pode ser negativa. Por favor, digite um valor válido.\n");
        } else if (distancia_km == 0 && (strcmp(distancia_km_str, "0") != 0 && strcmp(distancia_km_str, "0.0") != 0)) {
            // Verifica se atof retornou 0 devido a uma entrada inválida e não porque o usuário digitou '0'
            printf("Entrada inválida. Por favor, digite um número para a distância.\n");
        }
        else {
            break; // Sai do loop se a entrada for válida
        }
    }

    // Calcular o tempo em segundos
    tempo_segundos = distancia_km / VELOCIDADE_LUZ_KM_POR_SEGUNDO;

    // Converter para outras unidades de tempo
    tempo_minutos = tempo_segundos / 60.0;
    tempo_horas = tempo_minutos / 60.0;
    tempo_dias = tempo_horas / 24.0;

    printf("\nDistância informada: %.2f km\n", distancia_km);
    printf("Velocidade da luz: %.3f km/s\n", VELOCIDADE_LUZ_KM_POR_SEGUNDO);
    printf("\n--- Tempo de Viagem da Luz ---\n");
    printf("Em segundos: %.2f s\n", tempo_segundos);
    printf("Em minutos: %.2f min\n", tempo_minutos);
    printf("Em horas: %.2f h\n", tempo_horas);
    printf("Em dias: %.2f dias\n", tempo_dias);

    return 0; // Indica que o programa terminou com sucesso
}