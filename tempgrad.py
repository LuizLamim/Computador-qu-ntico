def calcular_gradiente_simples(T1, x1, T2, x2, unidade_T="°C", unidade_x="m"):
    """
    Calcula o gradiente de temperatura entre dois pontos.

    Args:
        T1 (float): Temperatura no ponto 1.
        x1 (float): Posição no ponto 1.
        T2 (float): Temperatura no ponto 2.
        x2 (float): Posição no ponto 2.
        unidade_T (str): Unidade de temperatura (ex: "°C", "K").
        unidade_x (str): Unidade de distância (ex: "m", "cm").

    Returns:
        float: O valor do gradiente de temperatura.
    """

    if x2 == x1:
        return "Erro: A distância não pode ser zero."

    # Calcula a variação de temperatura e distância
    delta_T = T2 - T1
    delta_x = x2 - x1

    # Calcula o gradiente
    gradiente = delta_T / delta_x

    print(f"--- Detalhes do Cálculo ---")
    print(f"Variação de Temperatura ($\Delta T$): {delta_T:.2f} {unidade_T}")
    print(f"Variação de Posição ($\Delta x$): {delta_x:.2f} {unidade_x}")
    print(f"Gradiente de Temperatura: {gradiente:.4f} {unidade_T}/{unidade_x}")

    return gradiente

# --- Exemplo de Uso ---
T_inicial = 25.0  # Temperatura inicial em °C
x_inicial = 0.0   # Posição inicial em metros (m)

T_final = 40.0    # Temperatura final em °C
x_final = 0.5     # Posição final em metros (m)

gradiente = calcular_gradiente_simples(T_inicial, x_inicial, T_final, x_final)

# Exemplo 2: Temperatura diminuindo ao longo da distância
print("\n" + "="*30 + "\n")
T_A = 100.0  # Temperatura em uma extremidade de uma barra (K)
x_A = 0.0    # Posição (cm)


T_B = 50.0   # Temperatura na outra extremidade da barra (K)
x_B = 10.0   # Posição (cm)

gradiente_2 = calcular_gradiente_simples(T_A, x_A, T_B, x_B, unidade_T="K", unidade_x="cm")