import numpy as np

class Perceptron:
    def __init__(self, taxa_aprendizado=0.01, n_iteracoes=100):
        """
        Inicializa o Perceptron.

        Args:
            taxa_aprendizado (float): A taxa na qual os pesos são ajustados durante o treinamento.
            n_iteracoes (int): O número de passagens completas sobre o conjunto de dados de treinamento.
        """
        self.taxa_aprendizado = taxa_aprendizado
        self.n_iteracoes = n_iteracoes
        self.pesos = None
        self.bias = None
        self.erros_por_iteracao = [] # Para armazenar o número de erros em cada iteração

    def _funcao_ativacao(self, x):
        """
        Função de ativação degrau (step function).
        Retorna 1 se a entrada for >= 0, caso contrário, retorna 0.
        """
        return np.where(x >= 0, 1, 0)

    def treinar(self, X, y):
        """
        Treina o Perceptron usando o conjunto de dados fornecido.

        Args:
            X (np.ndarray): Matriz de características de entrada, onde cada linha é uma amostra
                            e cada coluna é uma característica.
            y (np.ndarray): Vetor de rótulos de destino (0 ou 1) para cada amostra.
        """
        n_amostras, n_caracteristicas = X.shape

        # Inicializa os pesos e o bias com valores pequenos e aleatórios
        self.pesos = np.random.rand(n_caracteristicas) * 0.01
        self.bias = np.random.rand(1) * 0.01

        print("Iniciando treinamento...")
        print(f"Pesos iniciais: {self.pesos}, Bias inicial: {self.bias}")

        for iteracao in range(self.n_iteracoes):
            n_erros = 0
            for indice, x_i in enumerate(X):
                # Calcular a saída do Perceptron
                net_input = np.dot(x_i, self.pesos) + self.bias
                previsao = self._funcao_ativacao(net_input)

                # Calcular o erro
                erro = y[indice] - previsao

                # Se houver erro, ajustar os pesos e o bias
                if erro != 0:
                    self.pesos += self.taxa_aprendizado * erro * x_i
                    self.bias += self.taxa_aprendizado * erro
                    n_erros += 1

            self.erros_por_iteracao.append(n_erros)
            print(f"Iteração {iteracao + 1}/{self.n_iteracoes}: Erros = {n_erros}")
            if n_erros == 0:
                print("Convergência alcançada! Nenhum erro nesta iteração.")
                break # Se não houver erros, o modelo aprendeu

        print("Treinamento concluído.")
        print(f"Pesos finais: {self.pesos}, Bias final: {self.bias}")

    def prever(self, X):
        """
        Faz previsões usando o Perceptron treinado.

        Args:
            X (np.ndarray): Matriz de características de entrada para previsão.

        Returns:
            np.ndarray: Vetor de previsões (0 ou 1) para cada amostra.
        """
        net_input = np.dot(X, self.pesos) + self.bias
        previsoes = self._funcao_ativacao(net_input)
        return previsoes

---

## Exemplo de Uso

Vamos usar um exemplo simples para demonstrar como treinar e usar o Perceptron. Usaremos o problema do "E Lógico" (AND gate), que o Perceptron consegue resolver.

```python
if __name__ == "__main__":
    # Dados para o problema "AND gate"
    # X: Entradas (x1, x2)
    # y: Saídas esperadas (x1 AND x2)
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    y = np.array([0, 0, 0, 1])

    # Criar e treinar o Perceptron
    perceptron = Perceptron(taxa_aprendizado=0.1, n_iteracoes=10)
    perceptron.treinar(X, y)

    print("\n--- Testando o Perceptron ---")
    # Fazer previsões
    previsoes = perceptron.prever(X)
    print(f"Entradas:\n{X}")
    print(f"Saídas esperadas: {y}")
    print(f"Previsões do Perceptron: {previsoes}")

    # Você pode testar com novas entradas
    nova_entrada = np.array([[0, 1]])
    previsao_nova = perceptron.prever(nova_entrada)
    print(f"\nPrevisão para entrada {nova_entrada}: {previsao_nova[0]}")

    nova_entrada_2 = np.array([[1, 0]])
    previsao_nova_2 = perceptron.prever(nova_entrada_2)
    print(f"Previsão para entrada {nova_entrada_2}: {previsao_nova_2[0]}")

    nova_entrada_3 = np.array([[1, 1]])
    previsao_nova_3 = perceptron.prever(nova_entrada_3)
    print(f"Previsão para entrada {nova_entrada_3}: {previsao_nova_3[0]}")