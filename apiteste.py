from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Produto(BaseModel):
    nome: str
    preco: float
    em_estoque: bool = True

    @app.get("/")
def home():
    return {"mensagem": "API rodando com sucesso no VS Code!"}

@app.get("/produtos/{item_id}")
def ler_item(item_id: int):
    return {"item_id": item_id, "nome": "Item de Exemplo"}

@app.post("/produtos/")
def criar_produto(produto: Produto):
    return {
        "status": "Produto criado",
        "produto_recebido": produto.nome,
        "valor": produto.preco
    }