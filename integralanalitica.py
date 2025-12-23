import scipy.integrate as integrate
import numpy as np

# Definimos a função como uma função Python normal (lambda ou def)
# f(x) = x^2
def f(x):
    return x**2

# Calculando a integral de 0 a 3
# O quad retorna dois valores: (resultado, erro_estimado)
resultado, erro = integrate.quad(f, 0, 3)

print(f"O resultado da integral é: {resultado}")
# Saída: 9.0