import requests
from bs4 import BeautifulSoup

def validar_perfil_esports(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return False, "❌ Não foi possível acessar o link."

        soup = BeautifulSoup(response.text, "html.parser")
        texto = soup.get_text().lower()

        palavras_chave = ["furia", "e-sports", "esports", "csgo", "counter-strike"]

        if any(palavra in texto for palavra in palavras_chave):
            return True, "✅ Perfil validado como fã de e-sports!"
        else:
            return False, "❌ Perfil não relacionado a e-sports."
    except Exception as e:
        return False, f"Erro ao validar: {e}"

