# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# num3 = float(input("Digite o terceiro número: "))

# resultado = num1 + num2 + num3

# print(f"A soma de {num1} + {num2} + {num3} é igual a: {resultado}")

numeros = []

print("Digite os números que deseja somar.")
print("Digite 'sair' (ou 's') quando terminar.\n")

while True:
    entrada = input("Digite um número: ")

    # 2. Verifica se o usuário quer parar
    # .lower() garante que funcione mesmo se digitar 'SAIR' ou 'Sair'
    if entrada.lower() in ['sair', 's']:
        break

    # 3. Tenta converter e adicionar à lista
    try:
        numero = float(entrada)
        numeros.append(numero)  # O .append() coloca o número dentro da lista
    except ValueError:
        print("Isso não parece um número válido. Tente novamente.")

# 4. Processa os resultados
if len(numeros) > 0:
    total = sum(numeros)  # A função sum() soma todos os itens da lista magicamente
    print("-" * 30)
    print(f"Você digitou os números: {numeros}")
    print(f"A soma total é: {total}")
else:
    print("Nenhum número foi digitado.")