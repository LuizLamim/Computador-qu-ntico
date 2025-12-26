#include <iostream>

using namespace std;

int main() {
    // Declaração da matriz 3x3
    int matriz[3][3];

    // Preenchendo a matriz com 0
    // O primeiro loop (i) controla as LINHAS
    for (int i = 0; i < 3; i++) {
        // O segundo loop (j) controla as COLUNAS
        for (int j = 0; j < 3; j++) {
            matriz[i][j] = 0;
        }
    }