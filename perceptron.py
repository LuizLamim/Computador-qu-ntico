import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        # Taxa de aprendizado: Controla o tamanho do ajuste nos pesos a cada iteração.
        self.learning_rate = learning_rate
        # Número de iterações: Quantas vezes o algoritmo vai passar pelos dados de treinamento.
        self.n_iterations = n_iterations
        # Pesos: Inicializados como None, serão definidos durante o treinamento.
        self.weights = None
        # Bias (viés): Um termo adicional que permite ao Perceptron mover a linha de decisão.
        self.bias = None

    def _activation_function(self, x):
        # Função de ativação degrau (step function).
        # Se a soma ponderada for maior ou igual a 0, a saída é 1. Caso contrário, é 0.
        return 1 if x >= 0 else 0

    def fit(self, X, y):
        # X: Matriz de características de entrada (dados de treinamento).
        # y: Vetor de rótulos (saídas esperadas).

        n_samples, n_features = X.shape

        # Inicializa os pesos e o bias com zeros.
        # Adiciona 1 ao número de características para incluir o bias diretamente como um peso.
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Loop de treinamento por um número definido de iterações.
        for _ in range(self.n_iterations):
            # Para cada amostra nos dados de treinamento:
            for idx, x_i in enumerate(X):
                # Calcula a soma ponderada das entradas.
                # A "np.dot" realiza o produto escalar entre o vetor de entrada e o vetor de pesos.
                linear_output = np.dot(x_i, self.weights) + self.bias
                
                # Aplica a função de ativação para obter a previsão do Perceptron.
                y_predicted = self._activation_function(linear_output)

                # Calcula o erro: diferença entre a saída real e a saída prevista.
                update = y[idx] - y_predicted

                # Ajusta os pesos e o bias.
                # Se a previsão estiver errada, os pesos são ajustados para "mover" a fronteira de decisão
                # na direção correta.
                self.weights += self.learning_rate * update * x_i
                self.bias += self.learning_rate * update

    def predict(self, X):
        # X: Matriz de características de entrada (dados para predição).

        # Calcula a soma ponderada para cada amostra em X.
        linear_output = np.dot(X, self.weights) + self.bias
        
        # Aplica a função de ativação para cada soma ponderada e retorna as previsões.
        y_predicted = [self._activation_function(x) for x in linear_output]
        return np.array(y_predicted)