def elevar_ao_cubo_exp(numero):

    return numero ** 3
try:
  entrada_usuario = float(input("Digite um número para elevar ao cubo: "))
except ValueError:
  print("Entrada inválida. Por favor, digite um número.")
else:
  resultado = elevar_ao_cubo_exp(entrada_usuario)
  print(f"O número {entrada_usuario} elevado ao cubo é: {resultado}")