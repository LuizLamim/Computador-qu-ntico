#include <iostream>

int main() {
    char primeiro_caractere = 'A';
    
    std::cout << "Os 13 primeiros caracteres do alfabeto (Maiúsculas) são:\n";

    for (int i = 0; i < 13; ++i) {
        char caractere_atual = primeiro_caractere + i;
        
        std::cout << caractere_atual << " ";
    }