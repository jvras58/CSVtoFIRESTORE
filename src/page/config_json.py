"""Tela de Configuração JSON para Firestore."""

import streamlit as st
import json

def show_page() -> None:
    """Mostra a página de configuração JSON para Firestore."""
    st.title("Configuração JSON para Firestore")
    
    json_file = st.file_uploader("Escolha um arquivo JSON de credenciais do Firebase", type="json")
    
    if json_file is not None:
        try:
            json_content = json_file.getvalue().decode("utf-8")
            json_data = json.loads(json_content)
            
            if json_data.get("type") == "service_account":
                st.session_state['firebase_config'] = json_content
                st.success("Arquivo JSON carregado com sucesso!")
            else:
                st.error('O certificado de conta de serviço é inválido. O certificado deve conter um campo "type" definido como "service_account".')
        except json.JSONDecodeError as e:
            st.error(f"Erro ao carregar o arquivo JSON: {e}")
    else:
        st.warning("Por favor, carregue um arquivo JSON de credenciais do Firebase.")
