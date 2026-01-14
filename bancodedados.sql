CREATE DATABASE SistemaEstoque;

USE SistemaEstoque;

CREATE TABLE Produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único automático
    nome VARCHAR(100) NOT NULL,         -- Nome do produto (texto)
    categoria VARCHAR(50),              -- Categoria (ex: Eletrônicos)
    preco DECIMAL(10, 2),               -- Preço com 2 casas decimais
    quantidade INT DEFAULT 0,           -- Quantidade em estoque (número inteiro)
    data_cadastro DATE                  -- Data que o produto entrou
);

INSERT INTO Produtos (nome, categoria, preco, quantidade, data_cadastro)
VALUES 
    ('Notebook Gamer', 'Eletrônicos', 4500.00, 10, '2024-01-15'),
    ('Mouse Sem Fio', 'Acessórios', 120.50, 50, '2024-01-16'),
    ('Cadeira de Escritório', 'Móveis', 850.00, 5, '2024-01-20');

SELECT nome, quantidade 
FROM Produtos 
WHERE quantidade < 10;

SELECT nome, (preco * quantidade) AS valor_total_estoque
FROM Produtos;

UPDATE Produtos 
SET quantidade = quantidade - 1 
WHERE nome = 'Notebook Gamer';

DELETE FROM Produtos 
WHERE nome = 'Mouse Sem Fio';