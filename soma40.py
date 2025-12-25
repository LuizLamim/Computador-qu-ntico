# A função range(1, 41) gera números de 1 até 40
# (o último número, 41, é exclusivo/não entra)
#resultado = sum(range(1, 41))

#print(f"A soma dos 40 primeiros números é: {resultado}")

soma = 0

# Para cada número 'i' no intervalo de 1 a 40
for i in range(1, 41):
    soma += i  # Adiciona o valor de 'i' à variável 'soma'
    # É o mesmo que fazer: soma = soma + i

print(f"A soma é: {soma}")

n = 40
soma = (n * (n + 1)) // 2  # Usamos // para garantir divisão inteira

print(f"Calculado matematicamente: {soma}")