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