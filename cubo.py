def elevar_ao_cubo_exp(numero):

    return numero ** 3
try:
  entrada_usuario = float(input("Digite um número para elevar ao cubo: "))
except ValueError:
  print("Entrada inválida. Por favor, digite um número.")
else:
  resultado = elevar_ao_cubo_exp(entrada_usuario)
  print(f"O número {entrada_usuario} elevado ao cubo é: {resultado}")

print(f"5 elevado ao cubo é: {elevar_ao_cubo_exp(5)}")    # Saída: 125
print(f"2.5 elevado ao cubo é: {elevar_ao_cubo_exp(2.5)}") # Saída: 15.625
print(f"-3 elevado ao cubo é: {elevar_ao_cubo_exp(-3)}")  # Saída: -27