class DiscordLibrary:
    def __init__(self):
        self.users = {}  # {user_id: user_object}
        self.channels = {}  # {channel_id: channel_object}
        self.servers = {}  # {server_id: server_object}
        self.next_user_id = 1
        self.next_channel_id = 1
        self.next_server_id = 1

    def create_user(self, username):
        user_id = self.next_user_id
        user = {"id": user_id, "username": username, "status": "online"}
        self.users[user_id] = user
        self.next_user_id += 1
        print(f"Usuário '{username}' (ID: {user_id}) criado.")
        return user

    def get_user(self, user_id):
        return self.users.get(user_id)

    def update_user_status(self, user_id, new_status):
        user = self.get_user(user_id)
        if user:
            user["status"] = new_status
            print(f"Status do usuário '{user['username']}' atualizado para '{new_status}'.")
            return True
        print(f"Usuário com ID {user_id} não encontrado.")
        return False

    def create_server(self, name, owner_id):
        owner = self.get_user(owner_id)
        if not owner:
            print(f"Proprietário com ID {owner_id} não encontrado para criar o servidor.")
            return None

        server_id = self.next_server_id
        server = {
            "id": server_id,
            "name": name,
            "owner_id": owner_id,
            "members": {owner_id},  # Conjunto de IDs de membros
            "channels": {}  # {channel_id: channel_object}
        }
        self.servers[server_id] = server
        self.next_server_id += 1
        print(f"Servidor '{name}' (ID: {server_id}) criado por '{owner['username']}'.")
        return server

    def get_server(self, server_id):
        return self.servers.get(server_id)

    def add_member_to_server(self, server_id, user_id):
        server = self.get_server(server_id)
        user = self.get_user(user_id)
        if server and user:
            if user_id not in server["members"]:
                server["members"].add(user_id)
                print(f"Usuário '{user['username']}' adicionado ao servidor '{server['name']}'.")
                return True
            print(f"Usuário '{user['username']}' já é membro do servidor '{server['name']}'.")
            return False
        print("Servidor ou usuário não encontrado para adicionar membro.")
        return False

    def create_channel(self, server_id, channel_name, channel_type="text"):
        server = self.get_server(server_id)
        if not server:
            print(f"Servidor com ID {server_id} não encontrado para criar o canal.")
            return None

        channel_id = self.next_channel_id
        channel = {
            "id": channel_id,
            "name": channel_name,
            "type": channel_type,
            "server_id": server_id,
            "messages": []
        }
        self.channels[channel_id] = channel
        server["channels"][channel_id] = channel
        self.next_channel_id += 1
        print(f"Canal '{channel_name}' (ID: {channel_id}, Tipo: {channel_type}) criado no servidor '{server['name']}'.")
        return channel

    def get_channel(self, channel_id):
        return self.channels.get(channel_id)

    def send_message(self, channel_id, sender_id, content):
        channel = self.get_channel(channel_id)
        sender = self.get_user(sender_id)
        if channel and sender:
            message = {
                "sender_id": sender_id,
                "sender_username": sender["username"],
                "content": content,
                "timestamp": "AGORA"  # Em um sistema real, seria um datetime
            }
            channel["messages"].append(message)
            print(f"Mensagem enviada no canal '{channel['name']}' por '{sender['username']}': {content}")
            return True
        print("Canal ou remetente não encontrado para enviar mensagem.")
        return False

    def get_channel_messages(self, channel_id):
        channel = self.get_channel(channel_id)
        if channel:
            return channel["messages"]
        return []

# --- Exemplo de Uso ---
if __name__ == "__main__":
    discord_sim = DiscordLibrary()

    # 1. Criar Usuários
    user1 = discord_sim.create_user("Alice")
    user2 = discord_sim.create_user("Bob")
    user3 = discord_sim.create_user("Charlie")

    print("\n--- Informações dos Usuários ---")
    print(discord_sim.get_user(user1["id"]))
    discord_sim.update_user_status(user2["id"], "ausente")
    print(discord_sim.get_user(user2["id"]))

    # 2. Criar Servidor
    server1 = discord_sim.create_server("Meu Servidor Incrível", user1["id"])

    # 3. Adicionar Membros ao Servidor
    if server1:
        discord_sim.add_member_to_server(server1["id"], user2["id"])
        discord_sim.add_member_to_server(server1["id"], user3["id"])
        discord_sim.add_member_to_server(server1["id"], user3["id"]) # Tentando adicionar de novo

    # 4. Criar Canais
    if server1:
        channel_general = discord_sim.create_channel(server1["id"], "geral")
        channel_voice = discord_sim.create_channel(server1["id"], "voz-principal", "voice")

    # 5. Enviar Mensagens
    if channel_general:
        discord_sim.send_message(channel_general["id"], user1["id"], "Olá a todos!")
        discord_sim.send_message(channel_general["id"], user2["id"], "E aí, pessoal?")
        discord_sim.send_message(channel_general["id"], user3["id"], "Bom dia!")

    print("\n--- Mensagens do Canal Geral ---")
    for msg in discord_sim.get_channel_messages(channel_general["id"]):
        print(f"[{msg['timestamp']}] {msg['sender_username']}: {msg['content']}")

    print("\n--- Informações do Servidor ---")
    if server1:
        print(f"Nome do Servidor: {server1['name']}")
        print(f"Proprietário: {discord_sim.get_user(server1['owner_id'])['username']}")
        print(f"Membros IDs: {server1['members']}")
        print("Canais no Servidor:")
        for ch_id, ch_obj in server1["channels"].items():
            print(f"  - {ch_obj['name']} (ID: {ch_obj['id']}, Tipo: {ch_obj['type']})")

    # Exemplo de erro: tentar adicionar um membro inexistente
    discord_sim.add_member_to_server(server1["id"], 999)