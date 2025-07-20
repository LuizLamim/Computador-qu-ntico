def adicionar(x, y):
    """Função para adicionar dois números"""
    return x + y

def subtrair(x, y):
    """Função para subtrair dois números"""
    return x - y

def multiplicar(x, y):
    """Função para multiplicar dois números"""
    return x * y

def dividir(x, y):
    """Função para dividir dois números"""
    if y == 0:
        return "Erro! Divisão por zero não é permitida."
    else:
        return x / y

def calculadora():
    """Função principal da calculadora"""
    print("Selecione a operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

    while True:
        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite números.")
                continue

            if escolha == '1':
                print(f"{num1} + {num2} = {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
        elif escolha == '5':
            print("Obrigado por usar a calculadora! Até mais.")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente com 1, 2, 3, 4 ou 5.")

# Chamada da função da calculadora para iniciar
if __name__ == "__main__":
    calculadora()