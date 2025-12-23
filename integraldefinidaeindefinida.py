import sympy as sp

# 1. Definir a variável simbólica (o 'x' da equação)
x = sp.symbols('x')

# 2. Definir a função
# Exemplo: f(x) = x^2 + cos(x)
funcao = x**2 + sp.cos(x)

print(f"Função original: {funcao}")

# --- CÁLCULO DA INTEGRAL INDEFINIDA ---
# Sintaxe: sp.integrate(funcao, variavel)
resultado_indefinida = sp.integrate(funcao, x)

print("\nIntegral Indefinida:")
print(resultado_indefinida)
# Saída esperada: x**3/3 + sin(x)

# --- CÁLCULO DA INTEGRAL DEFINIDA ---
# Sintaxe: sp.integrate(funcao, (variavel, inicio, fim))
# Vamos calcular de 0 a 5
resultado_definida = sp.integrate(funcao, (x, 0, 5))

print("\nIntegral Definida (0 a 5):")
print(resultado_definida)
# O SymPy mantém o resultado exato (com frações e sin(5))

# Para ver o valor numérico decimal:
print(f"Valor numérico aproximado: {resultado_definida.evalf()}")