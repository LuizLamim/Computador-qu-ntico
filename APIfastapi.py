from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Definimos o "Modelo" do dado. Isso garante que o usuário
# só envie o que a gente permitir (segurança e validação).
class Tarefa(BaseModel):
    id: int
    titulo: str
    concluida: bool

# Nosso "banco de dados" fictício
banco_de_dados: List[Tarefa] = []

@app.get("/tarefas")
def listar_tarefas():
    return banco_de_dados

@app.post("/tarefas", status_code=201)
def criar_tarefa(tarefa: Tarefa):
    banco_de_dados.append(tarefa)
    return {"status": "Adicionado", "item": tarefa}