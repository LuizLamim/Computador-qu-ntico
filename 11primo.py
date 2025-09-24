import matplotlib.pyplot as plt

def gerar_primos(n):
    """
    Gera uma lista com os primeiros 'n' números primos.
    """
    # Inicializa a lista de primos
    primos = []
    # Começa a busca a partir do número 2 (o primeiro primo)
    numero_candidato = 2

    while len(primos) < n:
        
        eh_primo = True
        
        for divisor in range(2, int(numero_candidato**0.5) + 1):
            if numero_candidato % divisor == 0:
                # Se encontrar um divisor, não é primo
                eh_primo = False
                # Pula para o próximo número candidato
                break