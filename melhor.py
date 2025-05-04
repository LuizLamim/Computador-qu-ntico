def animate(i):
    angulo = 2 * np.pi * i / num_frames

    # Calcula as coordenadas do retângulo rotacionado
    x_ret = [-largura_retangulo / 2 * np.cos(angulo),
             largura_retangulo / 2 * np.cos(angulo),
             largura_retangulo / 2 * np.cos(angulo),
             -largura_retangulo / 2 * np.cos(angulo),
             -largura_retangulo / 2 * np.cos(angulo)]
    y_ret = [-altura_retangulo / 2 + largura_retangulo / 2 * np.sin(angulo),
             -altura_retangulo / 2 + largura_retangulo / 2 * np.sin(angulo),
             altura_retangulo / 2 + largura_retangulo / 2 * np.sin(angulo),
             altura_retangulo / 2 + largura_retangulo / 2 * np.sin(angulo),
             -altura_retangulo / 2 + largura_retangulo / 2 * np.sin(angulo)]
    retangulo.set_data(x_ret, y_ret)

    # Calcula as coordenadas das linhas que formam o cilindro
    for j, linha in enumerate(linhas_cilindro):
        theta = 2 * np.pi * j / num_linhas
        y_base = -altura_retangulo / 2 + j * (altura_retangulo / (num_linhas - 1))
        x_cil = [largura_retangulo / 2 * np.cos(angulo), largura_retangulo / 2 * np.cos(angulo + 2 * np.pi)]
        y_cil = [y_base + largura_retangulo / 2 * np.sin(angulo),
                 y_base + largura_retangulo / 2 * np.sin(angulo)]
        linha.set_data(x_cil * np.cos(theta) - y_cil * np.sin(theta),
                       x_cil * np.sin(theta) + y_cil * np.cos(theta))

    return [retangulo] + linhas_cilindro