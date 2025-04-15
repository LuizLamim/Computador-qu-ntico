import math

def calcular_area_elipse(a, b):
  """
  Calcula a área de uma elipse.

  Args:
    a: O comprimento do semieixo maior.
    b: O comprimento do semieixo menor.

  Returns:
    A área da elipse. Retorna None se os valores de a ou b forem não positivos.
  """
  if a <= 0 or b <= 0:
    print("Os comprimentos dos semieixos devem ser positivos.")
    return None
  return math.pi * a * b

# Obtém os valores dos semieixos do usuário
try:
  semieixo_maior = float(input("Digite o comprimento do semieixo maior (a): "))
  semieixo_menor = float(input("Digite o comprimento do semieixo menor (b): "))

  # Calcula a área da elipse
  area = calcular_area_elipse(semieixo_maior, semieixo_menor)

  # Exibe o resultado
  if area is not None:
    print(f"A área da elipse com semieixo maior {semieixo_maior} e semieixo menor {semieixo_menor} é: {area:.2f}")

except ValueError:
  print("Entrada inválida. Por favor, digite números para os comprimentos dos semieixos.")