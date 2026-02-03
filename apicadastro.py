from flask import Flask, jsonify, request

app = Flask(__name__)

# Nosso "banco de dados" temporário (na memória)
tarefas = [
    {"id": 1, "titulo": "Estudar Python", "concluida": False},
    {"id": 2, "titulo": "Criar uma API", "concluida": False}
]

# ROTA GET: Para listar todas as tarefas
@app.route('/tarefas', methods=['GET'])
def obter_tarefas():
    return jsonify(tarefas)

# ROTA POST: Para adicionar uma nova tarefa
@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.get_json() # Pega os dados enviados pelo usuário
    tarefas.append(nova_tarefa)
    return jsonify({"mensagem": "Tarefa adicionada com sucesso!", "dados": nova_tarefa}), 201

if __name__ == '__main__':
    app.run(debug=True)