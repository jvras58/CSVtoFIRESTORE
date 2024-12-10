"""Tela Tarefa 5: Exportação de Dados Json para o Firestore."""

import json

import streamlit as st

from utils.load import (
    initialize_firebase_from_session,
    load_toml,
    send_data_to_firestore,
)

labels = load_toml('ui_labels')


def upload_json_to_firestore() -> None:
    """Função para carregar e enviar dados de um arquivo JSON
    para uma coleção Firestore"""

    collection_name = st.text_input("Digite o nome da coleção no Firestore:")

    uploaded_file = st.file_uploader("Escolha um arquivo JSON", type="json")

    if st.button("Enviar Dados para o Firestore"):  # noqa: PLR1702
        if uploaded_file is not None and collection_name:
            db = initialize_firebase_from_session()
            if db is not None:
                try:
                    data = json.load(uploaded_file)
                    if isinstance(data, list):
                        for item in data:
                            send_data_to_firestore(db, collection_name, item)
                    elif isinstance(data, dict):
                        send_data_to_firestore(db, collection_name, data)
                    st.success(
                        f"Dados enviados com sucesso para a coleção "
                        f"'{collection_name}'!"
                    )
                except json.JSONDecodeError as e:
                    st.error(f"Erro ao carregar o JSON: {e}")
        else:
            st.error(
                "Por favor, selecione um arquivo JSON e insira o nome da "
                "coleção."
            )


def show_page() -> None:
    """Mostra a página Tarefa 1 com funcionalidade de upload para o
    Firestore."""

    st.title(labels['tarefa_5']['titulo'])
    st.write(labels['tarefa_5']['descricao'])

    upload_json_to_firestore()
