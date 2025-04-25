def calcular_coeficiente_dilatacao_volumetrica(volume_inicial, volume_final, temperatura_inicial, temperatura_final):
  """
  Calcula o coeficiente de dilatação volumétrica de um material.

  Args:
    volume_inicial (float): Volume inicial do material.
    volume_final (float): Volume final do material após a variação de temperatura.
    temperatura_inicial (float): Temperatura inicial do material (em Celsius ou Kelvin).
    temperatura_final (float): Temperatura final do material (na mesma unidade da temperatura inicial).

  Returns:
    float: O coeficiente de dilatação volumétrica.
           Retorna None se a variação de temperatura for zero para evitar divisão por zero.
  """
  delta_volume = volume_final - volume_inicial
  delta_temperatura = temperatura_final - temperatura_inicial

  if delta_temperatura == 0:
    print("A variação de temperatura é zero. Não é possível calcular o coeficiente de dilatação.")
    return None
  else:
    coeficiente_volumetrico = delta_volume / (volume_inicial * delta_temperatura)
    return coeficiente_volumetrico

# Exemplo de uso:
volume_inicial = 100.0  # cm^3
volume_final = 102.5   # cm^3
temperatura_inicial = 20.0 # Celsius
temperatura_final = 100.0 # Celsius

coeficiente = calcular_coeficiente_dilatacao_volumetrica(volume_inicial, volume_final, temperatura_inicial, temperatura_final)

if coeficiente is not None:
  print(f"O coeficiente de dilatação volumétrica é: {coeficiente:.6f} /°C")

# Outro exemplo com unidades diferentes de temperatura (Kelvin):
volume_inicial_k = 50.0  # m^3
volume_final_k = 50.3   # m^3
temperatura_inicial_k = 293.15 # Kelvin (20°C)
temperatura_final_k = 373.15   # Kelvin (100°C)

coeficiente_k = calcular_coeficiente_dilatacao_volumetrica(volume_inicial_k, volume_final_k, temperatura_inicial_k, temperatura_final_k)

if coeficiente_k is not None:
  print(f"O coeficiente de dilatação volumétrica (em Kelvin) é: {coeficiente_k:.6f} /K")