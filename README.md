
# 🎯 Know Your Fan - FURIA Esports

Este projeto tem como objetivo conhecer melhor os fãs da FURIA Esports, coletando e validando informações para oferecer experiências mais personalizadas.

A solução foi desenvolvida como um aplicativo web utilizando **Streamlit** em Python.

---

## 🚀 Funcionalidades

- 📋 **Cadastro de Fã**: Nome, CPF, País, Estado e interesses em e-sports
- 🆔 **Upload e Validação de Documento**: Validação via OCR (Tesseract)
- 🌐 **Vinculação de Redes Sociais**: Twitter, Instagram, Steam e Discord
- 🏆 **Validação de Perfis de E-Sports**: Validação de links públicos em HLTV e similares
- 📊 **Resumo Final do Perfil**: Visualização dos dados cadastrados

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12
- Streamlit
- Pandas
- Pytesseract (OCR)
- Pillow (Manipulação de imagens)
- Requests
- BeautifulSoup4

---

## 📦 Estrutura do Projeto

```
know_your_fan/
├── app.py
├── requirements.txt
├── dados_fas_furia.csv (gerado automaticamente)
├── utils/
│   ├── __init__.py
│   ├── ocr.py
│   ├── social.py
│   └── esports.py
```

---

## ⚙️ Como Rodar o Projeto

1. **Clone o repositório**:

```bash
git clone https://github.com/seu-usuario/know-your-fan-furia.git
cd know-your-fan-furia
```

2. **Crie e ative um ambiente virtual (opcional)**:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

4. **Configure o caminho do Tesseract no `ocr.py`**:

No arquivo `utils/ocr.py`, ajuste a linha:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

> ⚠️ Certifique-se de que o Tesseract OCR esteja instalado no seu sistema.

5. **Execute o app**:

```bash
streamlit run app.py
```

O navegador abrirá automaticamente.

---

## 🧪 Teste rápido

1. Preencha um cadastro básico.  
2. Faça upload de um documento (CPF ou RG).  
3. Vincule suas redes sociais.  
4. Valide um perfil em sites de e-sports.  
5. Visualize o resumo completo.

---

## 🙋‍♂️ Autor

Desenvolvido por **Lucas Vidigal** como parte de um desafio técnico para a FURIA Esports.

---

## 📌 Observações

- O upload de documentos utiliza OCR para validação textual.
- A validação de perfis de e-sports é feita via scraping de sites públicos (HLTV, Liquipedia).
- Os dados são armazenados em `dados_fas_furia.csv` para futura análise e segmentação.

---

# 🖤💛 GO FURIA!
