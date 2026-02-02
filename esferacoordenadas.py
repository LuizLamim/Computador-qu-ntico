import matplotlib.pyplot as plt
import numpy as np

def plotar_esfera(raio=1):
    fig = plt.subplots(figsize=(8, 8), subplot_kw={'projection': '3d'})
    ax = fig[1]

    # Criando os dados para a esfera (coordenadas esféricas)
    # u varia de 0 a 2*pi (longitude)
    # v varia de 0 a pi (latitude)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)