"""Função para exportar dados de uma coleção Firestore para um arquivo CSV"""

import pandas as pd
import streamlit as st

from utils.load import initialize_firebase_from_session


def export_firestore_data(
    collection_name: str, filters: list[tuple[str, str, str]] = None
) -> None:
    """
    Função para exportar dados de uma coleção Firestore para um arquivo CSV
    """
    db = initialize_firebase_from_session()
    if db is not None:
        try:
            query = db.collection(collection_name)
            if filters:
                for field_name, op_string, field_value in filters:
                    query = query.where(field_name, op_string, field_value)
            docs = query.stream()
            data = []
            for doc in docs:
                data.append(doc.to_dict())
            if data:
                df = pd.DataFrame(data)
                csv = df.to_csv(index=False).encode('utf-8')
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
