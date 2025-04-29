import streamlit as st
import pandas as pd
import os
from utils.ocr import extrair_texto_imagem, validar_documento
from utils.social import validar_link_social
from utils.esports import validar_perfil_esports

st.set_page_config(page_title="FURIA - Know Your Fan", page_icon="🎮")

st.title("🎯 FURIA - Know Your Fan")

menu = st.sidebar.selectbox("Navegar", ["Cadastro", "Upload de Documento", "Redes Sociais", "Perfis de E-Sports", "Resumo Final"])

caminho_csv = "dados_fas_furia.csv"

if "usuario" not in st.session_state:
    st.session_state.usuario = {}

if menu == "Cadastro":
    st.header("📋 Cadastro do Fã")
    nome = st.text_input("Nome Completo")
    cpf = st.text_input("CPF")
    pais = st.text_input("País")
    estado = st.text_input("Estado")
    interesses = st.text_area("Seus interesses em e-sports")

    if st.button("Salvar Cadastro"):
        if nome and cpf and pais and estado and interesses:
            st.session_state.usuario = {
                "Nome": nome,
                "CPF": cpf,
                "País": pais,
                "Estado": estado,
                "Interesses": interesses,
                "Twitter": "",
                "Instagram": "",
                "Steam": "",
                "Discord": "",
                "Documento Validado": "Não"
            }

            if os.path.exists(caminho_csv):
                df_existente = pd.read_csv(caminho_csv)
                df_novo = pd.DataFrame([st.session_state.usuario])
                df_resultado = pd.concat([df_existente, df_novo], ignore_index=True)
                df_resultado.to_csv(caminho_csv, index=False)
            else:
                df_novo = pd.DataFrame([st.session_state.usuario])
                df_novo.to_csv(caminho_csv, index=False)

            st.success(f"✅ Cadastro salvo para: {nome}")
            st.session_state["cpf"] = cpf
        else:
            st.warning("⚠️ Preencha todos os campos antes de salvar.")

elif menu == "Upload de Documento":
    st.header("🆔 Upload de Documento")

    arquivo = st.file_uploader("Envie seu documento (RG/CPF Frente)", type=["png", "jpg", "jpeg"])

    if arquivo is not None:
        st.image(arquivo, caption="Documento enviado", use_column_width=True)
        if st.button("Validar Documento"):
            with st.spinner('🔎 Extraindo e validando documento...'):
                texto_extraido = extrair_texto_imagem(arquivo)
                st.subheader("📝 Texto Extraído:")
                st.text_area("Texto:", texto_extraido, height=300)

                if validar_documento(texto_extraido):
                    st.success("✅ Documento validado com sucesso!")
                    if os.path.exists(caminho_csv):
                        df = pd.read_csv(caminho_csv)
                        if "CPF" in st.session_state.usuario:
                            cpf_usuario = st.session_state.usuario["CPF"]
                            df.loc[df["CPF"] == cpf_usuario, "Documento Validado"] = "Sim"
                            df.to_csv(caminho_csv, index=False)
                else:
                    st.error("❌ Documento inválido ou ilegível.")

elif menu == "Redes Sociais":
    st.header("🌐 Vincular Redes Sociais")

    twitter = st.text_input("Link do Twitter")
    instagram = st.text_input("Link do Instagram")
    steam = st.text_input("Link do Steam")
    discord = st.text_input("Usuário Discord (ex: usuario#1234)")

    if st.button("Salvar Redes Sociais"):
        if os.path.exists(caminho_csv) and "CPF" in st.session_state.usuario:
            df = pd.read_csv(caminho_csv)
            cpf_usuario = st.session_state.usuario["CPF"]

            mensagens = []

            if twitter:
                valido, msg = validar_link_social(twitter)
                mensagens.append(f"Twitter: {msg}")
                if valido:
                    df.loc[df["CPF"] == cpf_usuario, "Twitter"] = twitter

            if instagram:
                valido, msg = validar_link_social(instagram)
                mensagens.append(f"Instagram: {msg}")
                if valido:
                    df.loc[df["CPF"] == cpf_usuario, "Instagram"] = instagram

            if steam:
                valido, msg = validar_link_social(steam)
                mensagens.append(f"Steam: {msg}")
                if valido:
                    df.loc[df["CPF"] == cpf_usuario, "Steam"] = steam

            if discord:
                df.loc[df["CPF"] == cpf_usuario, "Discord"] = discord
                mensagens.append(f"Discord: ✅ Usuário salvo.")

            df.to_csv(caminho_csv, index=False)

            for mensagem in mensagens:
                st.info(mensagem)

elif menu == "Perfis de E-Sports":
    st.header("🏆 Validação de Perfis de E-Sports")

    perfil = st.text_input("Cole o link do seu perfil em sites de e-sports (HLTV, Liquipedia, etc.)")

    if st.button("Validar Perfil"):
        if perfil:
            with st.spinner('🔎 Validando perfil...'):
                valido, mensagem = validar_perfil_esports(perfil)
                if valido:
                    st.success(mensagem)
                else:
                    st.error(mensagem)
        else:
            st.warning("⚠️ Cole um link primeiro.")

elif menu == "Resumo Final":
    st.header("✅ Resumo do Seu Perfil")

    if os.path.exists(caminho_csv):
        df = pd.read_csv(caminho_csv)

        cpf_usuario = st.text_input("Digite seu CPF para ver o perfil", value=st.session_state.get("cpf", ""))

        if cpf_usuario:
            perfil_usuario = df[df["CPF"] == cpf_usuario]

            if not perfil_usuario.empty:
                st.success("✅ Cadastro encontrado!")
                st.dataframe(perfil_usuario)
            else:
                st.warning("⚠️ Nenhum cadastro encontrado para o CPF informado.")
        else:
            st.info("ℹ️ Insira seu CPF para visualizar seus dados.")
    else:
        st.warning("⚠️ Nenhum dado encontrado ainda. Faça o cadastro primeiro.")