import requests
import json

def call_api(
    url: str,
    method: str = 'GET',
    headers: dict = None,
    params: dict = None,
    data: dict = None,
    json_data: dict = None,
    timeout: int = 30
):
    """
    Função genérica para fazer requisições a uma API.

    Args:
        url (str): O URL do endpoint da API.
        method (str): O método HTTP (GET, POST, PUT, DELETE, etc.). Padrão é 'GET'.
        headers (dict): Um dicionário de cabeçalhos HTTP.
        params (dict): Um dicionário de parâmetros de query string para requisições GET.
        data (dict): Um dicionário ou string com dados para requisições POST/PUT (form-encoded).
        json_data (dict): Um dicionário com dados JSON para requisições POST/PUT (application/json).
        timeout (int): O tempo limite em segundos para a requisição. Padrão é 30.

    Returns:
        tuple: Uma tupla contendo (status_code, response_json_or_text).
               Retorna None para o segundo elemento em caso de erro na requisição.
    """
    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers, params=params, timeout=timeout)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers, data=data, json=json_data, timeout=timeout)
        elif method.upper() == 'PUT':
            response = requests.put(url, headers=headers, data=data, json=json_data, timeout=timeout)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, headers=headers, timeout=timeout)
        else:
            print(f"Erro: Método HTTP '{method}' não suportado por esta função genérica.")
            return None, None

        response.raise_for_status()  # Lança uma exceção para códigos de status HTTP 4xx/5xx

        # Tenta parsear a resposta como JSON, se possível
        try:
            return response.status_code, response.json()
        except json.JSONDecodeError:
            return response.status_code, response.text

    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
        if http_err.response:
            try:
                # Tenta obter detalhes do erro da resposta JSON, se disponível
                error_details = http_err.response.json()
                print(f"Detalhes do erro da API: {error_details}")
            except json.JSONDecodeError:
                print(f"Resposta de erro da API: {http_err.response.text}")
        return http_err.response.status_code if http_err.response else None, None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Erro de Conexão: {conn_err}")
        return None, None
    except requests.exceptions.Timeout as timeout_err:
        print(f"Tempo Limite Excedido: {timeout_err}")
        return None, None
    except requests.exceptions.RequestException as req_err:
        print(f"Erro Geral da Requisição: {req_err}")
        return None, None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None, None

# --- Exemplos de Uso ---

if __name__ == "__main__":
    print("--- Exemplo 1: GET em uma API pública (JSONPlaceholder) ---")
    # Este é um endpoint de teste para buscar posts
    jsonplaceholder_url = "https://jsonplaceholder.typicode.com/posts/1"
    status_code, data = call_api(jsonplaceholder_url, method='GET')

    if status_code:
        print(f"Status Code: {status_code}")
        if data:
            print("Dados Recebidos:")
            print(json.dumps(data, indent=2))
        else:
            print("Nenhum dado JSON na resposta.")
    print("\n" + "="*50 + "\n")

    print("--- Exemplo 2: POST em uma API pública (JSONPlaceholder) ---")
    # Este é um endpoint de teste para criar posts
    jsonplaceholder_post_url = "https://jsonplaceholder.typicode.com/posts"
    new_post_data = {
        "title": "Meu Novo Post",
        "body": "Este é o conteúdo do meu novo post.",
        "userId": 1
    }
    status_code, data = call_api(jsonplaceholder_post_url, method='POST', json_data=new_post_data)

    if status_code:
        print(f"Status Code: {status_code}")
        if data:
            print("Resposta da Criação do Post:")
            print(json.dumps(data, indent=2))
        else:
            print("Nenhum dado JSON na resposta de criação.")
    print("\n" + "="*50 + "\n")

    print("--- Exemplo 3: Requisição com Parâmetros (GET) ---")
    # Exemplo com parâmetros de query string
    params_url = "https://jsonplaceholder.typicode.com/posts"
    query_params = {"userId": 1, "_limit": 2} # Buscar posts do usuário 1, limitar a 2
    status_code, data = call_api(params_url, method='GET', params=query_params)

    if status_code:
        print(f"Status Code: {status_code}")
        if data:
            print("Posts do Usuário 1 (limitado a 2):")
            print(json.dumps(data, indent=2))
        else:
            print("Nenhum dado JSON na resposta.")
    print("\n" + "="*50 + "\n")

    print("--- Exemplo 4: Requisição com Cabeçalhos Personalizados ---")
    # Exemplo com cabeçalhos customizados (um token de autorização fictício)
    headers_url = "https://jsonplaceholder.typicode.com/todos/1"
    custom_headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer seu_token_de_acesso_aqui" # Substitua pelo seu token real
    }
    status_code, data = call_api(headers_url, method='GET', headers=custom_headers)

    if status_code:
        print(f"Status Code: {status_code}")
        if data:
            print("Dados Recebidos com Cabeçalhos:")
            print(json.dumps(data, indent=2))
        else:
            print("Nenhum dado JSON na resposta.")
    print("\n" + "="*50 + "\n")

    print("--- Exemplo 5: Requisição com Erro Simulado (404 Not Found) ---")
    # Tentando acessar um endpoint que não existe para ver o tratamento de erros
    error_url = "https://jsonplaceholder.typicode.com/nonexistent_path"
    status_code, data = call_api(error_url, method='GET')

    if status_code:
        print(f"Status Code: {status_code}")
        print("Resposta em caso de erro (pode ser vazia ou texto simples):")
        print(data)
    print("\n" + "="*50 + "\n")