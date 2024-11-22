"""Tela Tarefa 1: Envio de Dados CSV para o Firestore."""

import streamlit as st

from utils.load import (
    initialize_firebase_from_session,
    load_csv,
    load_toml,
    send_data_to_firestore,
)

labels = load_toml('ui_labels')


def upload_csv_to_firestore() -> None:
    """Função para carregar e enviar dados de um arquivo CSV
    para uma coleção Firestore"""

    collection_name = st.text_input("Digite o nome da coleção no Firestore:")

    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

    if st.button("Enviar Dados para o Firestore"):
        if uploaded_file is not None and collection_name:
            db = initialize_firebase_from_session()
            if db is not None:
                data = load_csv(uploaded_file)
                for _, row in data.iterrows():
                    send_data_to_firestore(db, collection_name, row.to_dict())
                st.success(
                    f"Dados enviados com sucesso para a coleção "
                    f"'{collection_name}'!"
                )
        else:
            st.error(
                "Por favor, selecione um arquivo CSV e insira o nome da "
                "coleção."
            )


def show_page() -> None:
    """Mostra a página Tarefa 1 com funcionalidade de upload para o
    Firestore."""

    st.title(labels['tarefa_1']['titulo'])
    st.write(labels['tarefa_1']['descricao'])

    upload_csv_to_firestore()
