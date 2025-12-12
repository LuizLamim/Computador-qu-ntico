import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func = self._unit_step_func
        self.weights = None
        self.bias = None

    def _unit_step_func(self, x):
        """Função de ativação Degrau (Heaviside step function)"""
        return np.where(x >= 0, 1, 0)

    def fit(self, X, y):
        """
        Treina o modelo com os dados.
        :param X: Matriz de entrada (amostras x características)
        :param y: Vetor de alvos (labels verdadeiros)
        """
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                
                # Calcular a saída linear: z = w * x + b
                linear_output = np.dot(x_i, self.weights) + self.bias
                
                # Aplicar função de ativação
                y_predicted = self.activation_func(linear_output)

                # Regra de atualização do Perceptron:
                # w = w + taxa * (real - previsto) * entrada
                update = self.lr * (y[idx] - y_predicted)
                
                self.weights += update * x_i
                self.bias += update

                