if __name__ == "__main__":
    # Dados de treinamento (Porta AND)
    # [0, 0] -> 0
    # [0, 1] -> 0
    # [1, 0] -> 0
    # [1, 1] -> 1
    X = np.array([[0,0], [0,1], [1,0], [1,1]])
    y = np.array([0, 0, 0, 1])

    # Criar e treinar o perceptron
    p = Perceptron(learning_rate=0.1, n_iters=10)
    p.fit(X, y)

    # Testar
    predictions = p.predict(X)
    
    print("Pesos aprendidos:", p.weights)
    print("Viés aprendido:", p.bias)
    print("Previsões do modelo:", predictions)
    print("Esperado (Real):   ", y)