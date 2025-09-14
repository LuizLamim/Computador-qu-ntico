import numpy as np
import matplotlib.pyplot as plt

# A função logarítmica de base 35
# Usamos a fórmula de mudança de base: log_b(x) = log_e(x) / log_e(b)
def log_base_35(x):
  return np.log(x) / np.log(35)

# Cria um intervalo de valores para o eixo x.
# O logaritmo é definido apenas para x > 0.
x_valores = np.linspace(0.1, 100, 400)

# Calcula os valores correspondentes de y para cada x
y_valores = log_base_35(x_valores)