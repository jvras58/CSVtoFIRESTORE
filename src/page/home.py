"""Tela Home Dashboard Interativo."""

import streamlit as st
from utils.load import load_toml,load_image

labels = load_toml('ui_labels')

def show_page() -> None:
    """Mostra a página Home do dashboard."""
    # Título do dashboard
    st.title(labels['home']['titulo'])
    st.write(labels['home']['introducao_painel'])

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            load_image('logo-sheets.png'),
            caption='Logo-sheets',
            use_column_width=True,
        )

    with col2:
        st.image(
            load_image('logo-firebase.png'),
            caption='logo-firebase',
            use_column_width=True,
        )

    st.subheader(labels['home']['subtitulo'])
    st.write(labels['home']['GitHub'])
