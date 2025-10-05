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