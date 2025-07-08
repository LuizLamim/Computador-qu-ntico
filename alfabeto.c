#include <stdio.h> 

int main() {
    char letra;

   
    printf("Alfabeto em letras minusculas:\n");
    for (letra = 'a'; letra <= 'z'; letra++) {
        printf("%c ", letra);
    }
    printf("\n\n"); 

    
    printf("Alfabeto em letras maiusculas:\n");
    for (letra = 'A'; letra <= 'Z'; letra++) {
        printf("%c ", letra);
    }
    printf("\n"); 

    return 0; 
}