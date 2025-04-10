import matplotlib.pyplot as plt
import numpy as np

def calcular_atracao_gravitacional(m1, m2, r):
  """
  Calcula a força de atração gravitacional entre duas massas.

  Args:
    m1 (float): Massa do primeiro objeto em kg.
    m2 (float): Massa do segundo objeto em kg.
    r (float): Distância entre os centros dos dois objetos em metros.

  Returns:
    float: A força de atração gravitacional em Newtons (N). Retorna None se r for zero.
  """
  G = 6.67430e-11  # Constante gravitacional universal (N m^2/kg^2)
  if r == 0:
    return None  # Evita divisão por zero
  F = (G * m1 * m2) / (r**2)
  return F

def plotar_atracao_gravitacional(m1, m2, r_min, r_max, num_pontos=100):
  """
  Plota o gráfico da força de atração gravitacional em função da distância.

  Args:
    m1 (float): Massa do primeiro objeto em kg.
    m2 (float): Massa do segundo objeto em kg.
    r_min (float): Distância mínima a ser considerada no gráfico em metros.
    r_max (float): Distância máxima a ser considerada no gráfico em metros.
    num_pontos (int): Número de pontos a serem calculados e plotados.
  """
  if r_min >= r_max or r_min <= 0:
    print("Erro: r_min deve ser menor que r_max e maior que zero.")
    return

  distancias = np.linspace(r_min, r_max, num_pontos)
  forcas = [calcular_atracao_gravitacional(m1, m2, r) for r in distancias]

  plt.figure(figsize=(10, 6))
  plt.plot(distancias, forcas, label=f'm1={m1} kg, m2={m2} kg')
  plt.xlabel('Distância (r) em metros (m)')
  plt.ylabel('Força de Atração Gravitacional (F) em Newtons (N)')
  plt.title('Atração Gravitacional de Newton vs. Distância')
  plt.grid(True)
  plt.legend()
  plt.show()

if __name__ == "__main__":
  # Exemplo de uso:
  massa1 = 1000  # kg (por exemplo, um carro)
  massa2 = 5.972e24  # kg (massa da Terra)
  distancia_minima = 10  # metros
  distancia_maxima = 1000000  # metros

  plotar_atracao_gravitacional(massa1, massa2, distancia_minima, distancia_maxima)

  # Você pode experimentar com diferentes valores de massa e distância:
  # massa_sol = 1.989e30
  # massa_terra = 5.972e24
  # distancia_min_sol_terra = 1e10
  # distancia_max_sol_terra = 2e11
  # plotar_atracao_gravitacional(massa_sol, massa_terra, distancia_min_sol_terra, distancia_max_sol_terra)