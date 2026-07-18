import os
import ssl
import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()


import streamlit as st
from hfapi_summarization import resumir
from hfapi_textgeneration import gerar_texto
from hfapi_chatcompletion import completar_chat

def gerador_texto(prompt):
    if prompt:
        st.write("gerador de texto")
        texto_resposta = gerar_texto(prompt)
        st.write(texto_resposta)

def resumidor_texto(prompt):
    if prompt:
        st.write("resumidor de texto")
        texto_resposta = resumir(prompt)
        st.write(texto_resposta)

def chat_ia(prompt):
        st.write("chat com IA")

        if 'mensagens' not in st.session_state:
                mensagens = [{"role": "system", "content": "Responda as perguntas de forma correta e precisa"}]
                st.session_state['mensagens'] = mensagens
        else: 
            mensagens = st.session_state['mensagens']
        if prompt:
            mensagem_usuario = {"role": "user", "content": prompt}
            mensagens.append(mensagem_usuario)
            mensagens = completar_chat(mensagens)
            print(mensagens)

            for dic_mensagem in mensagens:
                role = dic_mensagem["role"]
                content = dic_mensagem["content"]
                if role !=  "system":
                    with st.chat_message(role):
                        st.write(content)
                

def main11_app():
    st.header("IAs da Hugging Face", divider=True) #titulo da página
    st.markdown("Selecione a IA que deseja utilizar:")
    
    opcao = ["gerar texto", "resumir texto", "abrir chat"]
    ferramenta_selecionada = st.selectbox("selecione a ferramenta IA", options=opcao)
    prompt = st.chat_input("Digite o prompt para gerar o texto (ou Ctrl+C para sair): ")

    if ferramenta_selecionada == "gerar texto":
        gerador_texto(prompt)
    elif ferramenta_selecionada == "resumir texto":
        resumidor_texto(prompt)
    elif ferramenta_selecionada == "abrir chat":
        chat_ia(prompt)

main11_app()