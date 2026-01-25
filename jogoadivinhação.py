import random

def jogo_adivinhacao():
    print("--- Bem-vindo ao Jogo de Adivinhação! ---")
    print("Estou pensando em um número entre 1 e 100.")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        try:
            palpite = int(input("Qual é o seu palpite? "))
            tentativas += 1

            if palpite < numero_secreto:
                print("Mais alto! Tente novamente.")
            elif palpite > numero_secreto:
                print("Mais baixo! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
                acertou = True
        except ValueError:
            print("Por favor, digite apenas números inteiros.")