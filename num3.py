num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

lista_numeros = [num1, num2, num3]

lista_numeros.sort(reverse=True)

print(f"Os dois maiores números são: {lista_numeros[0]} e {lista_numeros[1]}")