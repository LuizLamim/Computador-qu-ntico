import matplotlib

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

notas = n1 + n2 + n3 + n4
media = notas/ 4

if media >=5:
    print("Aprovado com:", media)
else:
    print("Reprovado com:", media)