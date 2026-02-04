from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# 1. Configuração do Banco de Dados
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. Modelo do Banco de Dados (Como a tabela será no SQLite)
class TarefaDB(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    concluida = Column(Boolean, default=False)

# Cria as tabelas de fato
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Função para abrir/fechar conexão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 3. Rotas da API
@app.post("/tarefas/")
def criar_tarefa(titulo: str, db: Session = Depends(get_db)):
    nova_tarefa = TarefaDB(titulo=titulo)
    db.add(nova_tarefa) # Adiciona no "carrinho"
    db.commit()         # Salva no arquivo
    db.refresh(nova_tarefa)
    return nova_tarefa

@app.get("/tarefas/")
def listar_tarefas(db: Session = Depends(get_db)):
    return db.query(TarefaDB).all() # Busca tudo no banco