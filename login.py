def verificar_login(usuarios, nome_usuario, senha):
    """Verifica se o nome de usuário e a senha fornecidos correspondem aos dados armazenados."""
    if nome_usuario in usuarios and usuarios[nome_usuario] == senha:
        return True
    else:
        return False

def programa_de_login():
    """Função principal para executar o programa de login."""
    usuarios = {
        "alice": "senha123",
        "bob": "senha456",
        "charlie": "senha789"
    }

    tentativas = 3
    while tentativas > 0:
        nome_usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")

        if verificar_login(usuarios, nome_usuario, senha):
            print("Login bem-sucedido!")
            break
        else:
            tentativas -= 1
            print(f"Login falhou. Você tem mais {tentativas} tentativa(s).")

    if tentativas == 0:
        print("Número máximo de tentativas excedido. Acesso negado.")

if __name__ == "__main__":
    programa_de_login()