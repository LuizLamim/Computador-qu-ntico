#include <stdio.h> // Biblioteca padrão de entrada e saída

// Função para adicionar dois números
double adicionar(double x, double y) {
    return x + y;
}

// Função para subtrair dois números
double subtrair(double x, double y) {
    return x - y;
}

// Função para multiplicar dois números
double multiplicar(double x, double y) {
    return x * y;
}

// Função para dividir dois números
double dividir(double x, double y) {
    if (y == 0) {
        // Retorna um valor especial para indicar erro, como NaN (Not a Number)
        // ou um número muito grande/pequeno para sinalizar o erro.
        // Para simplicidade, vamos usar um valor sentinel e imprimir a mensagem no main.
        return -1.0; // Um valor que você pode verificar no main para indicar erro
    } else {
        return x / y;
    }
}

int main() {
    int escolha;
    double num1, num2, resultado;

    printf("Selecione a operação:\n");
    printf("1. Adicionar\n");
    printf("2. Subtrair\n");
    printf("3. Multiplicar\n");
    printf("4. Dividir\n");
    printf("5. Sair\n");

    while (1) { // Loop infinito que será quebrado com 'break'
        printf("Digite sua escolha (1/2/3/4/5): ");
        scanf("%d", &escolha); // Lê a escolha do usuário

        if (escolha >= 1 && escolha <= 4) {
            printf("Digite o primeiro número: ");
            // %lf é usado para ler um double
            if (scanf("%lf", &num1) != 1) {
                printf("Entrada inválida. Por favor, digite um número.\n");
                // Limpa o buffer de entrada para evitar loop infinito em caso de entrada inválida
                while (getchar() != '\n');
                continue;
            }
            printf("Digite o segundo número: ");
            if (scanf("%lf", &num2) != 1) {
                printf("Entrada inválida. Por favor, digite um número.\n");
                while (getchar() != '\n');
                continue;
            }

            switch (escolha) {
                case 1:
                    resultado = adicionar(num1, num2);
                    printf("%.2lf + %.2lf = %.2lf\n", num1, num2, resultado);
                    break;
                case 2:
                    resultado = subtrair(num1, num2);
                    printf("%.2lf - %.2lf = %.2lf\n", num1, num2, resultado);
                    break;
                case 3:
                    resultado = multiplicar(num1, num2);
                    printf("%.2lf * %.2lf = %.2lf\n", num1, num2, resultado);
                    break;
                case 4:
                    resultado = dividir(num1, num2);
                    if (num2 == 0) {
                        printf("Erro! Divisão por zero não é permitida.\n");
                    } else {
                        printf("%.2lf / %.2lf = %.2lf\n", num1, num2, resultado);
                    }
                    break;
            }
        } else if (escolha == 5) {
            printf("Obrigado por usar a calculadora! Até mais.\n");
            break; // Sai do loop
        } else {
            printf("Escolha inválida. Por favor, tente novamente com 1, 2, 3, 4 ou 5.\n");
        }
    }

    return 0; // Indica que o programa terminou com sucesso
}