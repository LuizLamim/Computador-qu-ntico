import random

def jogo_adivinhacao():
    print("--- Bem-vindo ao Jogo de Adivinhação! ---")
    print("Estou pensando em um número entre 1 e 100.")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    