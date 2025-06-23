import string

print("Alfabeto Completo:")
print("---")

print("Letras Minúsculas:")
for letra in string.ascii_lowercase:
    print(letra, end=" ")
print("\n") # Adiciona uma linha em branco para separar

print("Letras Maiúsculas:")
for letra in string.ascii_uppercase:
    print(letra, end=" ")
print() # Quebra a linha no final