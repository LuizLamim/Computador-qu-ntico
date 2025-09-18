#include <stdio.h>
#include <math.h>

#define FILENAME "dados_cos.dat"
#define X_MIN -10.0
#define X_MAX 10.0
#define STEP 0.1

int main() {
    FILE *fp;
    double x, y;

    // Abrir o arquivo para escrita
    fp = fopen(FILENAME, "w");
    if (fp == NULL) {
        printf("Erro ao abrir o arquivo %s\n", FILENAME);
        return 1;
    }