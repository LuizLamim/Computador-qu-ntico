def calcular_aceleracao(velocidade_inicial, velocidade_final, tempo):
  """
  Calcula a aceleração (taxa de variação de velocidade).

  Argumentos:
    velocidade_inicial (float): A velocidade no início do intervalo de tempo.
    velocidade_final (float): A velocidade no final do intervalo de tempo.
    tempo (float): O tempo decorrido para a variação da velocidade.

  Retorna:
    float: A aceleração calculada.
  """
  aceleracao = (velocidade_final - velocidade_inicial) / tempo
  return aceleracao

def main():
  """
  Função principal para executar o programa.
  """
  print("--- Calculadora de Aceleração ---")
  print("A aceleração é a taxa de variação de velocidade ao longo do tempo.")

  try:
    # Solicita a entrada do usuário
    velocidade_inicial = float(input("Digite a velocidade inicial (em m/s): "))
    velocidade_final = float(input("Digite a velocidade final (em m/s): "))
    tempo = float(input("Digite o tempo decorrido (em segundos): "))

    # Verifica se o tempo é zero para evitar divisão por zero
    if tempo == 0:
      print("Erro: O tempo decorrido não pode ser zero.")
      return

    # Chama a função para calcular a aceleração
    aceleracao_calculada = calcular_aceleracao(velocidade_inicial, velocidade_final, tempo)

    # Exibe o resultado
    print(f"\nResultados:")
    print(f"Velocidade Inicial: {velocidade_inicial} m/s")
    print(f"Velocidade Final: {velocidade_final} m/s")
    print(f"Tempo Decorrido: {tempo} s")
    print(f"A Aceleração é: {aceleracao_calculada:.2f} m/s²")
    print("---------------------------------")

  except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
  except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Executa a função principal quando o script é rodado
if __name__ == "__main__":
  main()