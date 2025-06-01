import numpy as np
import matplotlib.pyplot as plt

def k_ar_dating(ar_k_ratio):
    """
    Calcula a idade de uma amostra usando a equação de datação K-Ar.

    Args:
        ar_k_ratio (float or np.array): Proporção de 40Ar* / 40K na amostra.

    Returns:
        float or np.array: Idade da amostra em anos.
    """
    # Constantes de decaimento do Potássio-40
    # Lambda total (soma de lambda_e e lambda_beta)
    lambda_total = 5.543e-10  # anos^-1
    lambda_e = 0.581e-10      # anos^-1 (captura eletrônica)
    lambda_beta = 4.962e-10   # anos^-1 (decaimento beta)

    # Termo de correção para as diferentes constantes de decaimento
    correction_term = (1 + lambda_e / lambda_beta) / (lambda_e / lambda_beta)
    
    # Aplicar a equação de datação
    # Para evitar log de zero ou valores negativos que não fariam sentido físico
    if isinstance(ar_k_ratio, np.ndarray):
        ar_k_ratio[ar_k_ratio < 0] = 0  # Garante que a proporção não seja negativa
    elif ar_k_ratio < 0:
        ar_k_ratio = 0
    
    age = (1 / lambda_total) * np.log(1 + ar_k_ratio * correction_term)
    return age

# Gerar uma série de proporções 40Ar* / 40K para plotagem
# Usaremos um intervalo que represente idades geológicas típicas
ar_k_ratios = np.linspace(0.001, 10, 500) # De 0.001 a 10 para abranger diversas idades

# Calcular as idades correspondentes
ages = k_ar_dating(ar_k_ratios)

# Converter idades para bilhões de anos (Ga) para melhor visualização
ages_ga = ages / 1e9

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(ar_k_ratios, ages_ga, linestyle='-', color='blue')
plt.title('Equação de Datação K-Ar: Idade vs. Proporção $^{40}$Ar$^{*}$/$^{40}$K')
plt.xlabel('Proporção $^{40}$Ar$^{*}$/$^{40}$K')
plt.ylabel('Idade (Bilhões de Anos - Ga)')
plt.grid(True)
plt.axvline(x=0, color='grey', linestyle='--', linewidth=0.8)
plt.axhline(y=0, color='grey', linestyle='--', linewidth=0.8)
plt.xlim(0, 10) # Limitar o eixo X para melhor visualização
plt.ylim(0, max(ages_ga) * 1.05) # Ajustar limite superior do eixo Y
plt.text(7, 4, r'$\lambda = 5.543 \times 10^{-10} \text{ anos}^{-1}$', fontsize=10, color='black')
plt.text(7, 3.5, r'$\frac{\lambda_e}{\lambda_\beta} = \frac{0.581 \times 10^{-10}}{4.962 \times 10^{-10}}$', fontsize=10, color='black')
plt.show()

# Exemplo de uso para um valor específico
sample_ar_k_ratio = 0.5
sample_age = k_ar_dating(sample_ar_k_ratio)
print(f"\nPara uma proporção de 40Ar*/40K de {sample_ar_k_ratio:.3f}, a idade da amostra é de {sample_age / 1e6:.2f} milhões de anos.")

sample_ar_k_ratio_2 = 5.0
sample_age_2 = k_ar_dating(sample_ar_k_ratio_2)
print(f"Para uma proporção de 40Ar*/40K de {sample_ar_k_ratio_2:.3f}, a idade da amostra é de {sample_age_2 / 1e9:.2f} bilhões de anos.")