#include <stdio.h>

int main() {
    // Definir a massa (m) como uma constante
    float massa = 10.0; // em kg
    
    // Abrir o arquivo para escrita
    FILE *arquivo = fopen("dados.txt", "w");
    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }
    
    // Escrever o cabeçalho no arquivo
    fprintf(arquivo, "Aceleracao\tForca\n");
    
    // Gerar os dados para aceleração de 0 a 10
    for (int i = 0; i <= 100; i++) {
        float aceleracao = (float)i / 10.0; // de 0.0 a 10.0
        float forca = massa * aceleracao;   // F = m * a
        
        // Escrever os dados no arquivo
        fprintf(arquivo, "%.2f\t\t%.2f\n", aceleracao, forca);
    }
    
    // Fechar o arquivo
    fclose(arquivo);
    
    printf("Dados gerados com sucesso no arquivo 'dados.txt'.\n");
    printf("Você pode usar um software como Gnuplot ou Excel para plotar o gráfico.\n");
    
    return 0;
}