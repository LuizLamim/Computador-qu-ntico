#include <stdio.h>
#include <math.h>

int main() {
    // Abre o arquivo para escrita. 'w' significa write.
    FILE *fp = fopen("dados.dat", "w");

    // Verifica se o arquivo foi aberto com sucesso.
    if (fp == NULL) {
        printf("Erro ao abrir o arquivo!\n");
        return 1;
    }