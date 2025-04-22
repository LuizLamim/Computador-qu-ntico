def calcular_aceleracao(velocidade_inicial, velocidade_final, tempo_inicial, tempo_final):
  """Calcula a aceleração média.

  Args:
    velocidade_inicial: Velocidade no instante inicial (em m/s).
    velocidade_final: Velocidade no instante final (em m/s).
    tempo_inicial: Instante de tempo inicial (em segundos).
    tempo_final: Instante de tempo final (em segundos).

  Returns:
    A aceleração média (em m/s²). Retorna None se o intervalo de tempo for zero.
  """
  delta_velocidade = velocidade_final - velocidade_inicial
  delta_tempo = tempo_final - tempo_inicial

  if delta_tempo == 0:
    return None  # Evita divisão por zero
  else:
    aceleracao = delta_velocidade / delta_tempo
    return aceleracao

# Exemplo de uso:
v_inicial = 10  # m/s
v_final = 25   # m/s
t_inicial = 2    # s
t_final = 7      # s

resultado_aceleracao = calcular_aceleracao(v_inicial, v_final, t_inicial, t_final)

if resultado_aceleracao is not None:
  print(f"A aceleração média é: {resultado_aceleracao:.2f} m/s²")
else:
  print("O intervalo de tempo não pode ser zero.")