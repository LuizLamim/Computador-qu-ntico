def somar_tres_consecutivos(primeiro_numero):
 
    segundo_numero = primeiro_numero + 1
    terceiro_numero = primeiro_numero + 2
    soma = primeiro_numero + segundo_numero + terceiro_numero


   return soma, primeiro_numero, segundo_numero, terceiro_numero

while True:
    try:
        num_inicial = int(input("Digite o primeiro de 3 números consecutivos: "))
        break  
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

resultado, n1, n2, n3 = somar_tres_consecutivos(num_inicial)

print("\n--- Resultado ---")
print(f"Os três números consecutivos são: **{n1}**, **{n2}** e **{n3}**")
print(f"A soma de {n1} + {n2} + {n3} é: **{resultado}**")