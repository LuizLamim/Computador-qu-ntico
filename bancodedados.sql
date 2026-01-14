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