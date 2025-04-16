import math

def calcular_volume_esfera(raio):
  """Calcula o volume de uma esfera dado o seu raio.

  Args:
    raio: O raio da esfera (um número).

  Returns:
    O volume da esfera (um número).
    Retorna None se o raio for negativo.
  """
  if raio < 0:
    print("O raio não pode ser negativo.")
    return None
  volume = (4/3) * math.pi * (raio ** 3)
  return volume

# Obtém o raio do usuário
try:
  raio_str = input("Digite o raio da esfera: ")
  raio = float(raio_str)

  # Calcula o volume
  volume_esfera = calcular_volume_esfera(raio)

  # Exibe o resultado
  if volume_esfera is not None:
    print(f"O volume da esfera com raio {raio} é: {volume_esfera:.2f}")

except ValueError:
  print("Entrada inválida. Por favor, digite um número para o raio.")