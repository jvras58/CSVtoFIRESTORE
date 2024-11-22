"""Tela Tarefa 3: Exportação de Dados CSV do Firestore."""

import streamlit as st

from utils.export_csv import export_firestore_data
from utils.load import load_toml

labels = load_toml('ui_labels')


def export_firestore_csv() -> None:
    """Função para exportar dados de uma coleção Firestore
    para um arquivo CSV"""

    with st.form(key='export_form'):
        collection_name = st.text_input(
            "Digite o nome da coleção no Firestore:"
        )
        filters = []
        field_name = st.text_input(
            "Digite o nome do campo para filtrar (opcional):"
        )
        # TODO: Adicionar opção de filtro de outros operadores não funcionaria
        # pois o firebase está somente com dados do tipo string
        op_string = st.selectbox(
            "Selecione o operador de filtro:",
            ["==", "!="]
        )
        field_value = st.text_input(
            "Digite o valor do campo para filtrar (opcional):"
        )
        if field_name and field_value:
            filters.append((field_name, op_string, field_value))

        submit_button = st.form_submit_button(
            label="Exportar Dados do Firestore"
        )

    if submit_button:
        if collection_name:
            export_firestore_data(collection_name, filters)
        else:
            st.error("Por favor, insira o nome da coleção.")


def show_page() -> None:
    """Mostra a página Tarefa 3 com funcionalidade de exportação
    para o Firestore."""

    st.title(labels['tarefa_3']['titulo'])
    st.write(labels['tarefa_3']['descricao'])

    export_firestore_csv()
