import requests

def validar_link_social(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=8)

        if response.status_code == 200:
            return True, "✅ Link válido!"
        else:
            return False, f"❌ Link inválido (Status {response.status_code})"
    except Exception as e:
        return False, f"❌ Erro ao validar link: {e}"
