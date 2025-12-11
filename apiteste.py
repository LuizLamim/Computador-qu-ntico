from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

lass Produto(BaseModel):
    nome: str
    preco: float
    em_estoque: bool = True