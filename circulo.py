import math

def calcular_area_circulo(raio):
  """Calcula a área de um círculo dado o raio."""
  area = math.pi * raio**2
  return area

# Exemplo de uso
raio = float(input("Digite o raio do círculo: "))
area = calcular_area_circulo(raio)
print(f"A área do círculo é: {area:.2f}")