"""Tela Tarefa 3: Exportação de Dados CSV para multiplas collections."""


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

    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

    field_mappings = {}
    collection_mappings = {}

    if uploaded_file is not None:
        data = load_csv(uploaded_file)
        st.write("Pré-visualização dos dados:")
        st.write(data.head())

        columns = data.columns.tolist()
        st.write(
            "Mapeie as colunas do CSV para os campos e coleções do Firestore:"
        )
        for column in columns:
            field = st.text_input(
                f"Campo Firestore para a coluna '{column}':"
            )
            collection = st.text_input(
                f"Coleção Firestore para a coluna '{column}':"
            )
            if field and collection:
                field_mappings[column] = field
                collection_mappings[column] = collection

    if st.button("Enviar Dados para o Firestore"):
        if (
            uploaded_file is None
            or not field_mappings
            or not collection_mappings
        ):
            st.error(
                "Por favor, selecione um arquivo CSV e mapeie as colunas "
                "para os campos e coleções."
            )
            return

        db = initialize_firebase_from_session()
        if db is None:
            return

        for _, row in data.iterrows():
            for col in columns:
                if col in field_mappings and col in collection_mappings:
                    document = {field_mappings[col]: row[col]}
                    send_data_to_firestore(
                        db, collection_mappings[col], document
                    )
        st.success(
            "Dados enviados com sucesso para as coleções especificadas!"
        )


def show_page() -> None:
    """Mostra a página Tarefa 3 com funcionalidade de upload para o
    Firestore."""

    st.title(labels['tarefa_3']['titulo'])
    st.write(labels['tarefa_3']['descricao'])

    upload_csv_to_firestore()
