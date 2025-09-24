import matplotlib.pyplot as plt

def gerar_primos(n):
    """
    Gera uma lista com os primeiros 'n' números primos.
    """
    # Inicializa a lista de primos
    primos = []
    # Começa a busca a partir do número 2 (o primeiro primo)
    numero_candidato = 2