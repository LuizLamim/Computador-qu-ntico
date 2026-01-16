db.usuarios.insertOne({
  nome: "Ana Silva",
  email: "ana@email.com",
  vip: true,
  endereco: { rua: "Av. Paulista, 1000", cidade: "São Paulo" },
  interesses: ["tecnologia", "livros"]
})

db.produtos.insertOne({
  nome: "Notebook Gamer X",
  preco: 4500.00,
  categoria: "Eletrônicos",
  detalhes: { ram: "16GB", cpu: "i7" },
  tags: ["computador", "gaming"]
})