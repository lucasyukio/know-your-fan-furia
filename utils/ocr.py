import pytesseract
from PIL import Image
import tempfile
import os

pytesseract.pytesseract.tesseract_cmd = r"D:\New folder\tesseract.exe"  # Ajuste para seu PC

def extrair_texto_imagem(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_filename = tmp_file.name

    img = Image.open(temp_filename)
    texto = pytesseract.image_to_string(img, lang='por')

    os.remove(temp_filename)
    return texto

def validar_documento(texto_extraido):
    palavras_chave = ["Nome", "Identidade", "CPF", "Nascimento"]
    return any(palavra.lower() in texto_extraido.lower() for palavra in palavras_chave)
