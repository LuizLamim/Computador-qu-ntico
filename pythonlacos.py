frutas = ["Maçã", "Banana", "Cereja"]

for fruta in frutas:
    print(f"Eu gosto de {fruta}")

    # O range(5) gera números de 0 a 4
for i in range(5):
    print(f"Contagem: {i}")

    contador = 0

while contador < 5:
    print(f"O contador é: {contador}")
    contador += 1  # Importante incrementar para evitar loop infinito

for numero in range(10):
    if numero == 3:
        continue  # Pula o 3 e continua o loop
    if numero == 8:
        break     # Para o loop totalmente ao chegar no 8
    
    print(numero)

cesta = ["Maçã", "Banana"]

for fruta in cesta:
    if fruta == "Uva":
        print("Achei uva!")
        break
else:
    print("Não encontrei uvas na cesta.") 
    # Isso será impresso porque o loop terminou sem usar 'break'