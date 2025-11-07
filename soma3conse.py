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