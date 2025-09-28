import requests

# URL base da API
BASE_URL = "https://exemplo.com/api"

# 1. Login para obter token
login_url = f"{BASE_URL}/login"
login_data = {
    "username": "meu_usuario",
    "password": "minha_senha"
}

response = requests.post(login_url, json=login_data)

if response.status_code == 200:
    token = response.json().get("token")  # supondo que a API devolva um token
    print("Login bem-sucedido! Token:", token)
else:
    print("Falha no login:", response.text)
    exit()

# 2. Atualizar senha (com token de autenticação)
update_url = f"{BASE_URL}/usuario/alterar-senha"
headers = {
    "Authorization": f"Bearer {token}",  # envio do token no header
    "Content-Type": "application/json"
}
update_data = {
    "senha_antiga": "minha_senha",
    "nova_senha": "senha_nova123"
}

response = requests.put(update_url, json=update_data, headers=headers)

if response.status_code == 200:
    print("Senha atualizada com sucesso!")
else:
    print("Erro ao atualizar senha:", response.text)