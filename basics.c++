#include <iostream> // Biblioteca para entrada e saída (input/output)
#include <string>   // Biblioteca para trabalhar com strings
#include <vector>   // Biblioteca para usar vetores (arrays dinâmicos)

// --- Definição de Funções ---

// Função simples que não retorna nada (void) e não recebe argumentos.
void saudarUsuario() {
    std::cout << "Olá! Bem-vindo ao programa C++ básico." << std::endl;
}

// Função que recebe um argumento e retorna um valor.
int somarNumeros(int a, int b) {
    return a + b;
}

// Função que demonstra o uso de um argumento por referência.
// Altera o valor da variável original passada.
void dobrarValor(int &numero) {
    numero = numero * 2;
    std::cout << "Dentro da função dobrarValor, o número é: " << numero << std::endl;
}

// --- Função Principal (main) ---
// Onde a execução do programa começa.
int main() {
    // 1. Saída de Dados (Output)
    std::cout << "--- 1. Saída de Dados ---" << std::endl;
    std::cout << "Este é um exemplo de saída de texto para o console." << std::endl;
    std::cout << "Uma nova linha é adicionada com std::endl." << std::endl;
    std::cout << "-------------------------" << std::endl << std::endl;

    // 2. Variáveis e Tipos de Dados
    std::cout << "--- 2. Variáveis e Tipos de Dados ---" << std::endl;
    int idade = 30; // Tipo inteiro
    double preco = 25.50; // Tipo ponto flutuante de dupla precisão
    char letra = 'C'; // Tipo caractere
    bool isAtivo = true; // Tipo booleano (verdadeiro/falso)
    std::string nome = "Maria"; // Tipo string (texto)

    std::cout << "Nome: " << nome << std::endl;
    std::cout << "Idade: " << idade << std::endl;
    std::cout << "Preço: " << preco << std::endl;
    std::cout << "Letra: " << letra << std::endl;
    std::cout << "Ativo: " << isAtivo << std::endl;
    std::cout << "-------------------------------------" << std::endl << std::endl;

    // 3. Entrada de Dados (Input)
    std::cout << "--- 3. Entrada de Dados ---" << std::endl;
    int numeroUsuario;
    std::cout << "Por favor, digite um número inteiro: ";
    std::cin >> numeroUsuario; // Lê um inteiro do teclado
    std::cout << "Você digitou: " << numeroUsuario << std::endl;

    std::string cidadeUsuario;
    // Limpa o buffer de entrada para evitar problemas com std::getline após std::cin >>
    std::cin.ignore();
    std::cout << "Por favor, digite o nome da sua cidade: ";
    std::getline(std::cin, cidadeUsuario); // Lê uma linha inteira, incluindo espaços
    std::cout << "Sua cidade é: " << cidadeUsuario << std::endl;
    std::cout << "---------------------------" << std::endl << std::endl;

    // 4. Operadores Aritméticos
    std::cout << "--- 4. Operadores Aritméticos ---" << std::endl;
    int a = 10, b = 3;
    std::cout << "a = " << a << ", b = " << b << std::endl;
    std::cout << "Soma (a + b): " << a + b << std::endl;
    std::cout << "Subtração (a - b): " << a - b << std::endl;
    std::cout << "Multiplicação (a * b): " << a * b << std::endl;
    std::cout << "Divisão (a / b): " << a / b << " (divisão inteira)" << std::endl;
    std::cout << "Resto (a % b): " << a % b << std::endl;
    std::cout << "----------------------------------" << std::endl << std::endl;

    // 5. Estruturas Condicionais (if, else if, else)
    std::cout << "--- 5. Estruturas Condicionais ---" << std::endl;
    if (numeroUsuario > 10) {
        std::cout << "O número que você digitou é maior que 10." << std::endl;
    } else if (numeroUsuario == 10) {
        std::cout << "O número que você digitou é igual a 10." << std::endl;
    } else {
        std::cout << "O número que você digitou é menor que 10." << std::endl;
    }

    // Exemplo com operador ternário (shorthand if-else)
    std::string status = (idade >= 18) ? "Adulto" : "Menor de idade";
    std::cout << "Pela idade (" << idade << "), você é: " << status << std::endl;
    std::cout << "------------------------------------" << std::endl << std::endl;

    // 6. Laços de Repetição (Loops)
    std::cout << "--- 6. Laços de Repetição ---" << std::endl;

    // Loop for: para um número conhecido de iterações
    std::cout << "Loop for (contando de 0 a 4):" << std::endl;
    for (int i = 0; i < 5; ++i) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    // Loop while: enquanto uma condição for verdadeira
    std::cout << "Loop while (contando de 5 a 1):" << std::endl;
    int contador = 5;
    while (contador > 0) {
        std::cout << contador << " ";
        contador--; // Decrementa o contador
    }
    std::cout << std::endl;

    // Loop do-while: garante que o bloco seja executado pelo menos uma vez
    std::cout << "Loop do-while (contando de 1 a 1 com do-while):" << std::endl;
    int k = 1;
    do {
        std::cout << k << " ";
        k++;
    } while (k <= 0); // Condição falsa, mas executa uma vez
    std::cout << std::endl;
    std::cout << "-----------------------------" << std::endl << std::endl;

    // 7. Uso de Funções
    std::cout << "--- 7. Uso de Funções ---" << std::endl;
    saudarUsuario(); // Chamando a função sem argumentos

    int num1 = 7, num2 = 3;
    int resultadoSoma = somarNumeros(num1, num2); // Chamando a função com argumentos
    std::cout << "A soma de " << num1 << " e " << num2 << " é: " << resultadoSoma << std::endl;

    int valorOriginal = 10;
    std::cout << "Valor original antes de dobrar: " << valorOriginal << std::endl;
    dobrarValor(valorOriginal); // Chamando a função com passagem por referência
    std::cout << "Valor após chamar dobrarValor: " << valorOriginal << std::endl;
    std::cout << "-------------------------" << std::endl << std::endl;

    // 8. Arrays e Vetores (Vectors)
    std::cout << "--- 8. Arrays e Vetores ---" << std::endl;
    // Array estático (tamanho fixo)
    int numeros[5] = {10, 20, 30, 40, 50};
    std::cout << "Elemento na posição 0 do array: " << numeros[0] << std::endl;

    // Vetor (Array dinâmico - mais flexível)
    std::vector<std::string> frutas;
    frutas.push_back("Maçã"); // Adiciona elementos
    frutas.push_back("Banana");
    frutas.push_back("Laranja");

    std::cout << "Primeira fruta no vetor: " << frutas[0] << std::endl;
    std::cout << "Número de frutas no vetor: " << frutas.size() << std::endl;

    std::cout << "Listando todas as frutas:" << std::endl;
    for (const std::string& fruta : frutas) { // Loop for-each (C++11 em diante)
        std::cout << "- " << fruta << std::endl;
    }
    std::cout << "---------------------------" << std::endl << std::endl;

    // Retorna 0 para indicar que o programa foi executado com sucesso.
    return 0;
}