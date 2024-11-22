"""Tela Tarefa 3: Exportação de Dados CSV do Firestore."""

import streamlit as st
import pandas as pd
from utils.load import load_toml, initialize_firebase_from_session
from firebase_admin import firestore

labels = load_toml('ui_labels')

def export_firestore_csv() -> None:
    """Função para exportar dados de uma coleção Firestore para um arquivo CSV"""
    
    collection_name = st.text_input("Digite o nome da coleção no Firestore:")
    
    if st.button("Exportar Dados do Firestore"):
        if collection_name:
            db = initialize_firebase_from_session()
            if db is not None:
                try:
                    docs = db.collection(collection_name).stream()
                    data = []
                    for doc in docs:
                        data.append(doc.to_dict())
                    
                    if data:
                        df = pd.DataFrame(data)
                        csv = df.to_csv(index=False)
                        st.download_button(
                            label="Baixar CSV",
                            data=csv,
                            file_name=f"{collection_name}.csv",
                            mime="text/csv"
                        )
                        st.success("Dados exportados com sucesso!")
                    else:
                        st.warning("Nenhum documento encontrado na coleção.")
                except Exception as e:
                    st.error(f"Erro ao exportar dados: {e}")
        else:
            st.error("Por favor, insira o nome da coleção.")

def show_page() -> None:
    """Mostra a página Tarefa 3 com funcionalidade de exportação para o Firestore."""
    
    st.title(labels['tarefa_3']['titulo'])
    st.write(labels['tarefa_3']['descricao'])
    
    export_firestore_csv()
