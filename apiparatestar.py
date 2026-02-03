from flask import Flask, jsonify

app = Flask(__name__)

# Definimos a rota (endereço) e o método
@app.route('/saudar', methods=['GET'])
def home():
    dados = {
        "mensagem": "Olá! Esta é minha primeira API em Python.",
        "status": "sucesso"
    }
    return jsonify(dados) # Transforma o dicionário Python em um JSON

if __name__ == '__main__':
    app.run(debug=True)