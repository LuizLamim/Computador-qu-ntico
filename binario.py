# Usando a função built-in bin()
numero_decimal = 25
numero_binario_com_prefixo = bin(numero_decimal)
numero_binario_puro = numero_binario_com_prefixo[2:]  # Remove o "0b"
print(f"O número decimal {numero_decimal} em binário (com prefixo): {numero_binario_com_prefixo}")
print(f"O número decimal {numero_decimal} em binário (puro): {numero_binario_puro}")