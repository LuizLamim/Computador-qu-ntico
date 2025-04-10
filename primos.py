def eh_primo(numero):
  """Verifica se um número é primo."""
  if numero <= 1:
    return False
  if numero <= 3:
    return True
  if numero % 2 == 0 or numero % 3 == 0:
    return False
  i = 5
  while i * i <= numero:
    if numero % i == 0 or numero % (i + 2) == 0:
      return False
    i += 6
  return True

def encontrar_primos_ate(limite):
  """Encontra todos os números primos até o limite especificado."""
  primos = []
  for numero in range(2, limite + 1):
    if eh_primo(numero):
      primos.append(numero)
  return primos

if __name__ == "__main__":
  limite = 10000
  numeros_primos = encontrar_primos_ate(limite)
  print(f"Números primos até {limite}:")
  for primo in numeros_primos:
    print(primo)