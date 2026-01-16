db.usuarios.insertOne({
  nome: "Ana Silva",
  email: "ana@email.com",
  vip: true,
  endereco: { rua: "Av. Paulista, 1000", cidade: "São Paulo" },
  interesses: ["tecnologia", "livros"]
})