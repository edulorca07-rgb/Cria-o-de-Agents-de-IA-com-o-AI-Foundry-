import os
import streamlit as st
from groq import Groq

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Agente IA - Groq", page_icon="🤖", layout="centered"
)

st.title("🤖 Agente IA (Groq)")
st.write("Digite sua pergunta abaixo para receber a resposta do agente.")

# -----------------------------------------------------------------------------
# AUTENTICAÇÃO
# -----------------------------------------------------------------------------
api_key = st.sidebar.text_input("", type="password")

if not api_key:
    api_key = os.environ.get("")

# -----------------------------------------------------------------------------
# INTERFACE DE INPUT E SAÍDA
# -----------------------------------------------------------------------------
# Form para permitir o envio com a tecla 'Enter'
with st.form(key="meu_formulario"):
    pergunta = st.text_area(
        "Sua Pergunta:",
        placeholder="Digite algo aqui...",
        height=100,
    )
    botao_enviar = st.form_submit_button("Gerar Resposta")

# -----------------------------------------------------------------------------
# PROCESSAMENTO E EXIBIÇÃO DA SAÍDA
# -----------------------------------------------------------------------------
if botao_enviar:
    if not api_key:
        st.error(
            ""
        )
    elif not pergunta.strip():
        st.warning("⚠️ Por favor, digite uma pergunta antes de enviar.")
    else:
        client = Groq(api_key=api_key)

        with st.spinner("Processando resposta..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": pergunta}],
                    model="openai/gpt-oss-120b",
                )

                resposta = chat_completion.choices[0].message.content

                # Campo de Saída
                st.subheader("Saída:")
                st.markdown(resposta)

            except Exception as e:
                st.error(f"Erro ao chamar a API: {e}")