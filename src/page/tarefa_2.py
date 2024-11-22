
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

    if uploaded_file is not None:
        data = load_csv(uploaded_file)
        st.write("Pré-visualização dos dados:")
        st.write(data.head())

        columns = data.columns.tolist()
        field_mappings = {}
        st.write("Mapeie as colunas do CSV para os campos do Firestore:")
        for column in columns:
            field = st.text_input(f"Campo Firestore para a coluna '{column}':")
            if field:
                field_mappings[column] = field

    if st.button("Enviar Dados para o Firestore"):
        if uploaded_file is not None and collection_name and field_mappings:
            db = initialize_firebase_from_session()
            if db is not None:
                for _, row in data.iterrows():
                    document = {
                        field_mappings[col]: row[col]
                        for col in columns if col in field_mappings
                    }
                    send_data_to_firestore(db, collection_name, document)
                st.success(
                    f"Dados enviados com sucesso para a coleção "
                    f"'{collection_name}'!"
                )
        else:
            st.error(
                "Por favor, selecione um arquivo CSV, insira o nome da "
                "coleção e mapeie as colunas."
            )


def show_page() -> None:
    """Mostra a página Tarefa 1 com funcionalidade de upload para o
    Firestore."""

    st.title(labels['tarefa_1']['titulo'])
    st.write(labels['tarefa_1']['descricao'])

    upload_csv_to_firestore()
